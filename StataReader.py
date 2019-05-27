# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:50:46 2018

See also: https://github.com/johnyf/pycflow2dot

@author: Felix Pöge
"""
import re
import os
import sys


class StataReader:

    patterns_use = [
            ("use\\s+(.*), clear", {1: 'use'}),
            ("use\\s+(.*)\\s+if\\s*(.*), clear", {1: 'use'}),
            ("use\\s+(.*)using\\s+(.*), clear", {2: 'use'}),
            ("use\\s+(.*)using\\s+(.*)\\s+if\\s*(.*), clear", {2: 'use'}),
            ("joinby\\s+(.*)using\\s+(.*),", {2: 'use'}),
            ("merge\\s+(.*)using\\s+(.*),", {2: 'use'}),
            ("append\\s+using\\s+(.*)", {1: 'use'}),
            ("import\\s+delimited\\s+(.*),", {1: 'use_ext'}),
            ("import\\s+excel\\s+(.*),", {1: 'use_ext'}),
            ("^do\\s+(.*)(?:,)?", {1: 'do'}),
            ("\\s+do\\s+(.*)(?:,)?", {1: 'do'})
            ]
    patterns_save = [
            ("save\\s+(.*)", {1: 'save'}),
            ("save\\s+(.*),", {1: 'save'}),
            ("erase\\s+(.*)", {1: 'erase'}),
            ("copy\\s+\"(.*)\"\\s+\"(.*)\"\\s*,\\s*replace",
             {1: 'use', 2: 'save'}),
            ("tempfile\\s+(.*)", {1: 'tempfile'}),
            ("graph\\s+export\\s+(.*), replace", {1: 'export'}),
            ("graph\\s+export\\s+(.*),", {1: 'export'}),
            ("graph\\s+export\\s+(.*)", {1: 'export'}),
            ("file\\s+open\\s+(.*)\\s+using\\s+(.*),", {2: 'export'}),
            ("esttab\\s+(.*)\\s+using\\s+(.*),", {2: 'export'})
            ]

    patterns_ado = [
        ("execute_match,\\s*mergingkeys\\(.*\\)\\s*"
         + "deceaseddata\\((.*)\\)\\s*"
         + "deceaseduniquedata\\((.*)\\)\\s*"
         + "coinventordata\\((.*)\\)\\s*"
         + "coworkerdata\\((.*)\\)\\s*"
         + "outmatchdata\\((.*)\\)\\s*"
         + "outpseudodata\\((.*)\\)\\s*"
         + "outcoinventordata\\((.*)\\)\\s*"
         + "debugfile\\((.*)\\)",
         {1: 'use', 2: 'use', 3: 'use', 4: 'use',
          5: 'save', 6: 'save', 7: 'save', 8: 'export'})
            ]
    patterns_global = [
            "global (.*)=(.*)",
            "global (.*) (.*)"
            ]
    patterns_local = [
            "^\\s*local\\s+(\\w[\\w0-9_]*)\\s*(?:=)?\\s?\\s*(.*)",
            "args ([\\w_]*)"
            ]

    def __init__(self):
        self.patterns = self.patterns_use
        self.patterns.extend(self.patterns_save)
        self.patterns.extend(self.patterns_ado)
        self.parsed = {}
        self.globals = {}
        self.disregarded_nodes = []
        self.verbose_comments = False
        self.verbose_locals = False

    def parse_global_file(self, fname):
        """
        Read in the globals defined in a file for later usage.
        """
        with open(fname, "r") as f:
            lines = f.readlines()
        for line in lines:
            for pattern in self.patterns_global:
                pat = re.compile(pattern)
                m = pat.search(line)
                if m is None:
                    continue
                else:
                    g = m.group(2).strip()
                    g = g.replace("\\\\", "/").replace("\"", "")
                    g = g.replace("\\", "/")
                    self.globals[m.group(1).strip()] = g
                    break

    def disregard_node(self, node_name):
        """
        Mark a node to be disregarded (i.e. not used when writing the graph
        file)
        """
        if node_name not in self.disregarded_nodes:
            self.disregarded_nodes.append(node_name)

    def replace_globals(self, instr):
        for glob in sorted(self.globals.keys(), key=len, reverse=True):
            instr = instr.replace("${" + glob + "}", self.globals[glob])
        return instr

    def read_stata(self, fname, local=None):
        print("Processing %s" % os.path.split(fname)[-1])
        with open(fname, "r") as f:
            lines = f.readlines()

        self.parse_stata(fname, lines, local=local)
        self.postproc_stata(fname, local=local)

    def set_verbose_comments(self, verbose_comments):
        self.verbose_comments = verbose_comments

    def set_verbose_locals(self, verbose_locals):
        self.verbose_locals = verbose_locals

    def parse_stata(self, fname, lines, local=None):

        if local is None:
            local = {}

        n_multiline_comment = 0
        i = 0
        carryover = ""
        while i < len(lines):
            line = carryover + lines[i]

            # =================================================================
            # Handle comments
            # =================================================================

            # Multi-line comments
            startcomment_pos = line.find("/*")
            endcomment_pos = line.find("*/")

            # Both start- and end comments
            if startcomment_pos != -1 and endcomment_pos != -1:
                # xxx /* comment */ yyy -> xxx  yyy
                if startcomment_pos < endcomment_pos:
                    line = line[:startcomment_pos] + line[endcomment_pos+2:]
                    lines[i] = line
                    continue
                else:
                    # comment 1 */ xxx /* comment 2 -> xxx /* comment 2
                    # (repeat parsing)
                    line = line[endcomment_pos+2:]
                    lines[i] = line
                    n_multiline_comment -= 1
                    continue
            # Only start comment
            elif startcomment_pos != -1:
                line = line[:startcomment_pos]
                # Nothing to process, easy
                if len(line.strip()) == 0:
                    n_multiline_comment += 1
                    if self.verbose_comments:
                        print("Line %d: Going up to comment level %d"
                              % (i, n_multiline_comment))
                else:
                    if self.verbose_comments:
                        print("Line %d: Shift multiline to next line")
                    # Something in the line which needs to processed.
                    # Move the comment to the next line!
                    # The code will take care of it from there
                    lines[i+1] = "/* " + lines[i+1]
            # Only end comment
            elif endcomment_pos != -1:
                # Keep the remainder after the comment and re-process it
                line = line[endcomment_pos+2:]
                n_multiline_comment -= 1
                lines[i] = line
                if self.verbose_comments:
                    print("Line %d: Going down to comment level %d"
                          % (i, n_multiline_comment))
                continue

            # When in the multiline setting: Ignore the current line
            if n_multiline_comment > 0:
                i += 1
                continue
            elif n_multiline_comment < 0:
                print("Possible coding error: More closing comments than "
                      + "opening ones detected. Filename: %s Line: %d"
                        % (fname, i))

            # One-line comments
            # Comment: #
            if line.strip().startswith("*"):
                i += 1
                continue

            # Comment: ///
            slashpos = line.find("///")
            if slashpos != -1:
                line = line[:slashpos]
                i += 1
                if i == len(lines):
                    print("Triple slash comment at end of the file. "
                          + "Filename: %s" % fname)
                carryover = line
                continue
            else:
                carryover = ""

            # Comment: //
            if line.strip().startswith("//"):
                i += 1
                continue
            slashpos = line.find("//")
            if slashpos != -1:
                line = line[:slashpos]

            # Iterate over locals and see if something can be found
            for lpattern in self.patterns_local:
                pat = re.compile(lpattern)
                m = pat.search(line)
                if m is None:
                    continue
                local_name = m.group(1)
                if lpattern.find("local") != -1:
                    local_value = m.group(2)
                else:
                    local_value = ""
                local_value = self._replace_locals(local_value, local)
                local_value = self.replace_globals(local_value)
                local_value = self._replace_locals(local_value, local)
                local_value = local_value.strip().strip("\"")
                local[local_name] = local_value
                if self.verbose_locals:
                    print("Found local %s -> %s" % (local_name,
                                                    local_value))

            # Iterate over all patterns and try to find the best match
            best_pattern = None
            best_pattern_len = -1
            best_pattern_type = None
            for pattern in self.patterns:
                pat = re.compile(pattern[0])
                m = pat.search(line)
                if m is None:
                    continue
                if len(pattern[0]) > best_pattern_len:
                    best_pattern_len = len(pattern[0])
                    best_pattern = m
                    best_pattern_type = pattern[1]

            if fname not in self.parsed:
                self.parsed[fname] = {}

            # Add the best match (if any) to the list
            if best_pattern is not None:
                for key in best_pattern_type.keys():
                    pat_type = best_pattern_type[key]
                    pat_str = best_pattern.group(key)
                    pat_str = self._replace_locals(pat_str, local)
                    pat_str = self.replace_globals(pat_str)
                    pat_str = self._replace_locals(pat_str, local)
                    pat_str = pat_str.replace(".dta", "").strip().strip("\"")
                    self.parsed[fname][i+1+(key-1)/100] = (pat_type, pat_str)

            i += 1

    def _replace_locals(self, s, local):
        """
        Replace locals in a string.

        local is a dictionary of local -> replacement combintions.
        """
        if local is None:
            return s
        if s.find("`") == -1:
            return s
        s_prev = s
        for local_key in local.keys():
            local_from = "`" + local_key + "'"
            local_to = local[local_key]
            s = s.replace(local_from, local_to)
        if s != s_prev:
            if self.verbose_locals:
                print("Replaced local: %s -> %s" % (s_prev, s))
            return self._replace_locals(s, local)
        else:
            return s

    def postproc_stata(self, fname, local=None):
        """
        Do postprocessing:
            - Replace \\ by /
            - When a file is
            d, remove it from what happened before
             (+ some checks)
            - TODO: Processing of Globals

        """
        # Replace locals
        for i in sorted(self.parsed[fname].keys()):
            t = self.parsed[fname][i]
            self.parsed[fname][i] = (t[0], self._replace_locals(t[1],
                                                                local))

        # Replace \ by /
        for i in sorted(self.parsed[fname].keys()):
            t = self.parsed[fname][i]
            self.parsed[fname][i] = (t[0], t[1].replace("\\\\", "/")
                                               .replace("\\", "/")
                                               .replace("\"", ""))

        # If a file is first saved and then used, disregard the 'use'
        # part (as it happens within the same file)
        saved = []
        lines = sorted(self.parsed[fname].keys())
        for line in lines:
            ftype, file = self.parsed[fname][line]
            if ftype in ['save', 'export']:
                saved.append(file)
            elif ftype in ['use', 'use_ext']:
                if file in saved:
                    self.parsed[fname].pop(line)
        del saved
        del lines

        # For each erased file, see if it was saved during the processing of
        # this file
        # TODO: Check if the file was also used in another Stata file
        for i in sorted(self.parsed[fname].keys(), reverse=True):
            if i not in self.parsed[fname]:
                continue
            t = self.parsed[fname][i]
            if t[0] not in ['erase', 'tempfile']:
                continue

            t_find_list = []
            if t[0] == 'tempfile':
                t_find_list.append("`" + t[1] + "'")
            else:
                t_find_list.append(t[1])
                # Incorporate the two ways of writing globals
                v1 = re.sub("\\$\\{(\\w+)\\}", lambda m: "$" + m.group(1),
                            t[1])
                if v1 != t[1]:
                    t_find_list.append(v1)
                v1 = re.sub("\\$(\\w+)", lambda m: "${" + m.group(1) + "}",
                            t[1])
                if v1 != t[1]:
                    t_find_list.append(v1)
                # print("Try to erase %s" % t_find_list)

            # Hunt for references to the same file
            for t_find in t_find_list:
                for j in sorted(self.parsed[fname].keys(), reverse=True):
                    u = self.parsed[fname][j]
                    if j == i:
                        continue
                    if u[1] != t_find:
                        continue
                    # The file was used after it was erased.
                    if j > i and t[0] != "tempfile":
                        print("File %s was used after being erased." % t[1])
                    elif j > i and t[0] == "tempfile":
                        self.parsed[fname].pop(j)
                    else:
                        self.parsed[fname].pop(j)
            # Delete the 'erase' instruction itself
            self.parsed[fname].pop(i)

    def _exp_get_do_node(self, fname):
        return "\"%s\" [color=%s, URL=\"file:///%s\"]" % (
                os.path.split(fname)[1],
                self._ftype_to_color("do"),
                fname)

    def _ftype_to_color(self, ftype):
        if ftype == 'erase':
            return "red"
        if ftype == 'use':
            return "blue"
        if ftype == 'use_ext':
            return "lightblue"
        if ftype == "save":
            return "green"
        if ftype == "export":
            return "orange"
        if ftype == "do":
            return "black"

    def _exp_get_file_node(self, ftype, fname):
        color = self._ftype_to_color(ftype)

        return "\"%s\" [color=%s, URL=\"file:///%s\"]" % (
                os.path.split(fname)[1],
                color,
                fname)

    def export_graphviz(self, f):
        """
        Export for graphical display
        """
        f.write("digraph StataReaderGraph {\n")

        file_links = []
        file_nodes = []
        # In here, save for each type a dictionary of node names
        # For each node name, save all do-files that it is accessed by
        file_clusters = {
                    'use': {},
                    'use_ext': {},
                    'save': {},
                    'export': {},
                    'do': {},
                    'erase': {}}
        file_cluster_usage = {}
        file_cluster_nodetypes = {}

        """
        Get all the links to be written & write out all nodes
        """
        # Define Stata Code node
        for fname in self.parsed:
            f.write(self._exp_get_do_node(fname) + ";\n")
            fname_node = os.path.split(fname)[1]
            file_nodes.append(fname_node)

        for fname in self.parsed:
            fname_node = os.path.split(fname)[1]
            for i in sorted(self.parsed[fname].keys()):
                t = self.parsed[fname][i]
                fname_node2 = os.path.split(t[1])[1]

                # Check if the node is to be disregarded.
                if fname_node2 in self.disregarded_nodes:
                    continue

                # If the node has not been written, do so now
                if t[1] not in file_nodes:
                    f.write(self._exp_get_file_node(t[0], t[1]) + ";\n")
                    file_nodes.append(t[1])
                    file_cluster_nodetypes[fname_node2] = t[0]

                if t[0] in ["export", "save", "erase"]:
                    file_links.append((fname_node, fname_node2))
                else:
                    file_links.append((fname_node2, fname_node))
                # For the clustering list
                if fname_node2 not in file_clusters[t[0]]:
                    file_clusters[t[0]][fname_node2] = []
                if fname_node not in file_clusters[t[0]][fname_node2]:
                    file_clusters[t[0]][fname_node2].append(fname_node)
                if fname_node2 not in file_cluster_usage:
                    file_cluster_usage[fname_node2] = [fname_node]
                else:
                    file_cluster_usage[fname_node2].append(fname_node)

        """
        Determine which nodes need to be clustered together.
        This happens when nodes are only connected to a file. For clearer
        visibility, they should then be grouped.
        """

        """
        Write them out!
        """
        for cluster_type in file_clusters.keys():
            groups = {}
            for node in file_clusters[cluster_type].keys():
                node_connections = file_clusters[cluster_type][node]
                if len(node_connections) == 1:
                    file_for_node = node_connections[0]
                    if file_for_node not in groups:
                        groups[file_for_node] = []
                    if len(set(file_cluster_usage[node])) == 1:
                        if file_cluster_nodetypes[node] == cluster_type:
                            groups[file_for_node].append(node)

            for cluster in groups:
                if len(groups[cluster]) > 1:
                    f.write("subgraph cluster_%s_%s {\n"
                            % (cluster.replace(".", "_"), cluster_type))
                    f.write("   rank = same;\n")
                    for element in groups[cluster]:
                        f.write("   \"%s\";\n" % element)
                    f.write("   graph[style=dotted];\n")
                    f.write("}\n")

        # Write out code lines
        i = 0
        while i < len(file_links):
            link = file_links[i]

            has_backward = False
            j = i+1
            while j < len(file_links):
                if file_links[j][0] == link[1] and file_links[j][1] == link[0]:
                    has_backward = True
                    file_links.pop(j)
                    j -= 1
                elif file_links[j][0] == link[0] \
                        and file_links[j][1] == link[1]:
                    file_links.pop(j)
                    j -= 1
                j += 1

            fname_node2 = os.path.split(t[1])[1]

            if has_backward is False:
                f.write("\"%s\" -> \"%s\"\n" % (link[0], link[1]))
            else:
                f.write("\"%s\" -> \"%s\" [dir=\"both\"]\n"
                        % (link[0], link[1]))

            i += 1

        f.write("}\n")
