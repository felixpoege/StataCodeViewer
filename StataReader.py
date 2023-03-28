# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:50:46 2018

See also: https://github.com/johnyf/pycflow2dot

Required libraries:
    - graphviz

The module infers the file input-output structure of Stata files from the
Stata code.

The information deduced from the code is then visualized as a flowchart.

As an additional option, the module can read information given in headers
of non-Stata files about input and output files.

@author: Felix Pöge
"""
import re
import os
import sys
import math
import shutil
import pandas as pd
import networkx as nx
from graphviz import Source


class StataReader:
    """
    TODO: Separate colors for estimates use / estimates save ?
    """

    patterns_use = [
            ("u(s|se)?(old)?\\s+(.*)", {3: 'use'}),
            ("u(s|se)?(old)?\\s+(.*)using\\s*(.*)", {4: 'use'}),
            ("u(s|se)?(old)?\\s+(.*?),\\s*(encoding|keep|clear|replace)", {3: 'use'}),
            ("u(s|se)?(old)?\\s+(.*)using\\s+(.*?),\\s*(encoding|keep|clear|replace)", {4: 'use'}),
            ("u(s|se)?(old)?\\s+(.*)using\\s+(.*)\\s+if\\s*(.*?),\\s*(encoding|keep|clear|replace)", {4: 'use'}),
            ("sysu(s|se)?\\s+(.*)", {2: 'use'}),
            ("sysu(s|se)?\\s+(.*?), (clear|replace)", {2: 'use'}),
            ("sysu(s|se)?\\s+(.*)\\s+if\\s*(.*?),\\s*(clear|replace)", {2: 'use'}),
            ("sysu(s|se)?\\s+(.*)using\\s+(.*?),\\s*(clear|replace)", {3: 'use'}),
            ("sysu(s|se)?\\s+(.*)using\\s+(.*)\\s+if\\s*(.*?), (clear|replace)", {3: 'use'}),
            ("joinby\\s+(.*)using\\s+(.*)", {2: 'use'}),
            ("joinby\\s+(.*)using\\s+(.*?),\\s*(unm|_merge|nol|update|replace)", {2: 'use'}),
            ("merge\\s+(.*)using\\s+(.*)", {2: 'use'}),
            ("merge\\s+(.*)using\\s+(.*?),", {2: 'use'}),
            ("reclink[2]?\\s+(.*)using\\s+(.*?),", {2: 'use'}),
            ("append\\s+using\\s+(.*?),\\s*(keep|force|gen)", {1: 'use'}),
            ("append\\s+using\\s+(.*)", {1: 'use'}),
            ("import\\s+delimited\\s+(.*)", {1: 'use_ext'}),
            ("import\\s+delimited\\s+(.*?),", {1: 'use_ext'}),
            # Special case of the delimiter being a comma
            ("import\\s+delimited\\s+(.*?),(.*)delim[i]?[t]?[e]?[r]?[s]?\(\",", {1: 'use_ext'}),
            ("import\\s+delimited\\s+(.*)using(.*)", {2: 'use_ext'}),
            ("import\\s+delimited\\s+(.*)using(.*?),", {2: 'use_ext'}),
            ("infix\\s+(.*)using(.*?),", {2: 'use_ext'}),
            ("infix\\s+(.*)using(.*)", {2: 'use_ext'}),
            ("import\\s+excel\\s+(using\\s+)?(.*?),", {2: 'use_ext'}),
            ("insheet\\s+(.*)using\\s+(.*)", {2: 'use'}),
            ("^do\\s+(.*?)(?:,)?", {1: 'do'}),
            ("\\s+do\\s+(.*?)(?:,)?", {1: 'do'}),
            ("estimates use\\s+(.*)", {1: 'use'}),
            ("file\\s+open\\s+(.*)\\s+using\\s+(.*?),(.*?)read", {2: 'use_ext'}),
            ]
    patterns_save = [
            ("sa(v|ve)?(old)?\\s+(.*)", {3: 'save'}),
            ("sa(v|ve)?(old)?\\s+(.*?),", {3: 'save'}),
            ("erase\\s+(.*)", {1: 'erase'}),
            ("copy\\s+\"(.*)\"\\s+\"(.*)\"\\s*,\\s*replace",
             {1: 'use', 2: 'save'}),
            ("tempfile\\s+(.*)", {1: 'tempfile'}),
            ("graph\\s+export\\s+(.*?), replace(.*)?", {1: 'export'}),
            ("graph\\s+export\\s+(.*?),", {1: 'export'}),
            ("graph\\s+export\\s+(.*?)", {1: 'export'}),
            ("file\\s+open\\s+(.*)\\s+using\\s+(.*?),(.*?)write", {2: 'export'}),
            ("esttab\\s+(.*)\\s+using\\s+(.*?),", {2: 'export'}),
            ("outreg\\s+(.*)\\s+using\\s+(.*?),", {2: 'export'}),
            ("estimates save\\s+(.*)", {1: 'save'}),
            ("estimates save\\s+(.*?),", {1: 'save'}),
            ("export\\s+(delimited|excel)\\s+(.*?)", {2: 'export'}),
            ("export\\s+(delimited|excel)\\s+(.*?),", {2: 'export'}),
            ("export\\s+(delimited|excel)\\s+(.*?),", {2: 'export'}),
            ("export\\s+(delimited|excel)\\s+(.*)\\s*using(.*?),", {3: 'export'}),
            ("export\\s+(delimited|excel)\\s+(.*)\\s*using(.*?)", {3: 'export'}),
            ("outsheet\\s+using(.*)", {1: 'export'}),
            ("outsheet\\s+using(.*?),", {1: 'export'}),
            ]

    patterns_exclude = [
            ("^\\s*note:")
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
            "^\\s*global ([\\w0-9_]+)\\s*[= ]\\s*(.*)"
            ]
    patterns_local = [
            "^\\s*local\\s+(\\w[\\w0-9_]*)\\s*(?:=)?\\s?\\s*(.*)",
            "args ([\\w_]*)",
            "^\\s*tempfile\\s+(\\w[\\w0-9_\\s]*)\\s*"
            ]

    """
    Rules for shortening lists of numbers (in forvalues loops)

    All: Keep all entries
    FirstN: Keep first N entries
    First_Last: Keep first and last entry
    FirstN_Last: Keep first N entries and the last one

    numlist_first_n property gives the N
    """
    numlist_rule = 'FirstN_Last'
    numlist_first_n = 3

    DEFAULT_HEADERS = {
        'filetypes': ['.R', '.py'],
        'input': ['@Inputs:', '# Inputs:'],
        'output': ['@Outputs:', '# Outputs:'],
        'other': ['# Depends On:',
                  '# Other Notes:',
                  '@Depends On:',
                  '@Other Notes:']
        }

    def __init__(self,
                 cut_paths=False,
                 verbose_locals=False,
                 base_folder="",
                 header_patterns=None):
        """
        cut_paths: Only use filenames as nodes for code, input and output
                   files. This makes the display more clunky, but is necessary
                   if file names are not unique.

        base_folder: Folder of the Stata repository. Either set it directly or
            use read_folder to set it automatically.

        verbose_locals: Increase verbosity of local parsing.

        header_patterns: To use other files (e.g., R, Python) as an input,
            specify a dictionary as DEFAULT_HEADERS

        """
        self.patterns = self.patterns_use
        self.patterns.extend(self.patterns_save)
        self.patterns.extend(self.patterns_ado)
        self.parsed = {}
        self.globals = {}
        self.disregarded_nodes = []
        self.verbose_comments = False
        self.verbose_bef_pat = False
        self.verbose_locals = verbose_locals
        self.indent = "\t"
        self.cut_paths = cut_paths
        self.base_folder = base_folder
        self.header_patterns = header_patterns

    def _try_read_file(self, fname):
        try:
            with open(fname, "r", encoding='utf8') as f:
                lines = f.readlines()
            return lines
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError on {fname}. Try latin-1.")

            with open(fname, "r", encoding='latin1') as f:
                lines = f.readlines()
            return lines

    def parse_global_file(self, fname):
        """
        Read in the globals defined in a file for later usage.
        """
        lines = self._try_read_file(fname)

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
                    g = self.replace_globals(g)
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
            # Global replacement with curved brackets
            instr = instr.replace("${" + glob + "}", self.globals[glob])
            # Global replacement without curved bracket surrounding the global
            # name.
            instr = re.sub("\\$" + glob + "([ /\"])",
                           self.globals[glob] + "\\1",
                           instr)
        return instr

    def read_stata(self, fname,
                   local=None,
                   skip_globals=False):
        """
        Load and parse Stata file.

        skip_globals: Do not parse globals in the Stata file.
        """
        fname = fname.replace("\\", "/")

        if not skip_globals:
            self.parse_global_file(fname)

        print("Processing %s" % os.path.split(fname)[-1])
        lines = self._try_read_file(fname)

        self.parse_stata(fname, lines, local=local)
        self.postproc_stata(fname, local=local)

    def read_header(self, fname):
        """
        Parse the contents of a header of a non-Stata file (e.g. R, Py).
        How to parse the header is defined when initializing this the Reader
        class.

        Parameters
        ----------
        fname : Path to file.


        Returns
        -------
        None.

        """
        # Ensure that a definition of header patterns is given.
        assert self.header_patterns is not None
        assert 'input' in self.header_patterns
        assert 'output' in self.header_patterns

        print(f"Processing {os.path.split(fname)[-1]}")
        lines = self._try_read_file(fname)

        # Which part of the header is currently being parsed?
        # None, Input, Output
        reading_state = 'None'
        header_input = ""
        header_output = ""

        # Parse the header (input/output/other tags)
        for line in lines:
            for tag in self.header_patterns['input']:
                if line.startswith(tag):
                    reading_state = 'Input'
                    line = line[len(tag):]
                    break
            for tag in self.header_patterns['output']:
                if line.startswith(tag):
                    reading_state = 'Output'
                    line = line[len(tag):]
                    break
            for tag in self.header_patterns['other']:
                if line.startswith(tag):
                    reading_state = 'None'
                    line = line[len(tag):]
                    break

            # Some cleaning to avoid mistakes in compiling the graph
            line = line.replace("*", "\*")
            line = line.replace('"', "")

            if reading_state == 'Input':
                header_input += line + ","
            elif reading_state == 'Output':
                header_output += line + ","

        # Skip files with empty headers
        if header_input.strip() + header_input.strip() == "":
            return

        # Comprehend it ... add the header as a parsed file.
        if fname not in self.parsed:
            self.parsed[fname] = {}

        i = 0
        for finput in header_input.split(","):
            finput = finput.strip()
            if finput == "":
                continue
            if finput.endswith(".dta"):
                finput = finput[:-4]
                use_type = "use"
            else:
                use_type = "use_ext"
            self.parsed[fname][i] = (use_type, finput)
            i += 1

        i = 0
        for foutput in header_output.split(","):
            foutput = foutput.strip()
            if foutput == "":
                continue
            if foutput.endswith(".dta"):
                foutput = foutput[:-4]
                exp_type = "save"
            else:
                exp_type = "export"
            self.parsed[fname][100 + i] = (exp_type, foutput)
            i += 1



    def read_stata_master(self, fname,
                          local=None):
        """
        Load and parse a master.do file that was auto-generated by this
        program.

        """
        fname = fname.replace("\\", "/")

        print("Processing %s" % os.path.split(fname)[-1])
        lines = self._try_read_file(fname)

        # Replace the comments before and after the actual .do files
        # with use/save statements.
        # Like this, the globally required input files and the globally
        # generated output files can be read into the standard code.
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith("// Requires input file"):
                line = line.replace("// Requires input file ",
                                    'use "')
                line = line.strip() + '"'

            if line.startswith("// Creates output file"):
                line = line.replace("// Creates output file ",
                                    'save "')
                line = line.strip() + '"'
            lines[i] = line

        self.parse_stata(fname, lines, local=local)
        self.postproc_stata(fname, local=local)

    def set_verbose_comments(self, verbose_comments):
        self.verbose_comments = verbose_comments

    def set_verbose_locals(self, verbose_locals):
        self.verbose_locals = verbose_locals

    def _split_stata_namelist(self, namelist):
        return re.split("\\s+", namelist)

    def _split_stata_numlist(self, numlist):
        """
        Parse a Stata numlist.
        Parsing is conducted according to pre-set parsing rules in the
        header of this tool.
        """
        numlist = numlist.strip()
        # Parse list of the form 1/5 -> 1, 2, 3, 4, 5
        m1 = re.match("([0-9\\-]+)/([0-9\\-]+)", numlist)
        # Parse list of the form 5(-1)1 -> 5, 4, 3, 2, 1
        #                        1(1)5  -> 1, 2, 3, 4, 5
        m2 = re.match("([0-9\\-]+)\\(([0-9\\-]+)\\)([0-9\\-]+)", numlist)
        if m1:
            int1 = int(m1.group(1))
            int_iter = 1
            int2 = int(m1.group(2))
            if int1 == int2:
                return [int1]
            else:
                assert int2 > int1
        elif m2:
            int1 = int(m2.group(1))
            int_iter = int(m2.group(2))
            int2 = int(m2.group(3))
            if int1 == int2:
                return [int1]
            else:
                if int_iter > 0:
                    assert int2 > int1
                elif int_iter < 0:
                    assert int2 < int1
                else:
                    raise ValueError("int_iter should not be zero."
                                     + " Numlist has gap zero.")

        else:
            print(f"Warning: Cannot parse numlist {numlist}")
            return []

        """
        Numlists are parsed according to pre-set rules
        (defined in the header of this tool)
        TODO: Add initializer to __init__
        """
        if self.numlist_rule == 'All':
            num_first = True
            num_firstN = 9999
            num_last = True
        else:
            if self.numlist_rule.startswith("First"):
                num_first = True
            else:
                num_first = False
            if self.numlist_rule.startswith("FirstN"):
                num_firstN = self.numlist_first_n
            else:
                num_firstN = 0
            if self.numlist_rule.endswith("Last"):
                num_last = True
            else:
                num_last = False
        ret_num = []
        if num_first:
            ret_num.append(int1)
        cnt = 1

        def _valid(x, int1, int2, int_iter):
            if int_iter > 0:
                return x < int2
            elif int_iter < 0:
                return x > int2
            else:
                raise ValueError("int_iter should not be zero."
                                 + " Numlist has gap zero.")

        x = int1
        while _valid(x, int1, int2, int_iter):
            if cnt <= num_firstN:
                ret_num.append(x)
            else:
                break
            cnt += 1
            x += int_iter

        if num_last:
            ret_num.append(int2)

        return ret_num

    def parse_stata(self, fname, lines, local=None):
        """
        Parse a Stata file.
        """

        if local is None:
            local = {}

        bracket_level = 0

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

            # =================================================================
            # Handle brackets, loops and conditions (start)
            # =================================================================
            if line.strip().startswith("foreach"):

                m1 = re.search("foreach\\s+(.*)\\s+in\\s+(.*)\\s+\\{", line)
                m2 = "foreach\\s+(.*)\\s+of\\s+(var[l]?[i]?[s]?[t]?|new[l]?[i]?[s]?[t]?)\\s+(.*)\\s+\\{"
                m2 = re.search(m2, line)
                m3 = "foreach\\s+(.*)\\s+of\\s+local\\s+(.*)\\s+\\{"
                m3 = re.search(m3, line)
                m3g = "foreach\\s+(.*)\\s+of\\s+global\\s+(.*)\\s+\\{"
                m3g = re.search(m3g, line)
                m4 = "foreach\\s+(.*)\\s+of\\s+num[l]?[i]?[s]?[t]?\\s+(.*)\\s+\\{"
                m4 = re.search(m4, line)
                if m1 is not None:
                    lcl_name = m1.group(1)
                    lcl_vals = self._split_stata_namelist(m1.group(2))
                    local[lcl_name] = {
                            'bracket_level': bracket_level+1,
                            'local_values': lcl_vals
                            }
                    bracket_level += 1
                    if self.verbose_locals:
                        print(f"Found foreach local: {lcl_name} -> {lcl_vals}")
                # This pattern is tricky, as it can depend on the content
                # of the dataset in memory at the time.
                # Basically, if there is a * or - in the varlist, then we can't
                # do anything about it.
                elif m2 is not None:
                    lcl_name = m2.group(1)
                    lcl_vals = self._split_stata_namelist(m2.group(3))
                    lcl_test = "".join(lcl_vals)
                    if lcl_test.find("*") != -1 or lcl_test.find("-") != -1:
                        print("Warning: foreach varlist local cannot be "
                              + "parsed due to wildcard in the variable "
                              + "list.")
                    else:
                        local[lcl_name] = {
                                'bracket_level': bracket_level+1,
                                'local_values': lcl_vals
                                }
                    bracket_level += 1
                    if self.verbose_locals:
                        print(f"Found foreach local: {lcl_name} -> {lcl_vals}")
                # TODO: Implement the replacement of local/global values
                elif m3 is not None:
                    bracket_level += 1
                elif m3g is not None:
                    bracket_level += 1
                elif m4 is not None:
                    lcl_name = m4.group(1)
                    lcl_vals = self._split_stata_numlist(m4.group(2))
                    if len(lcl_vals) > 0:
                        lcl_vals = [str(x) for x in lcl_vals]
                        local[lcl_name] = {
                                'bracket_level': bracket_level+1,
                                'local_values': lcl_vals
                                }
                        if self.verbose_locals:
                            print("Found foreach local: "
                                  + f"{lcl_name} -> {lcl_vals}")
                    bracket_level += 1
                else:
                    raise ValueError(f"Unknown foreach loop: {line}")

            if line.strip().startswith("forvalues"):
                m1 = "forvalues\\s+(.*)\\s+=\\s+(.*)\\s+\\{"
                m1 = re.search(m1, line)
                if m1 is not None:
                    lcl_name = m1.group(1)
                    lcl_vals = self._split_stata_numlist(m1.group(2))
                    lcl_vals = [str(x) for x in lcl_vals]
                    if len(lcl_vals) > 0:
                        local[lcl_name] = {
                                'bracket_level': bracket_level+1,
                                'local_values': lcl_vals
                                }
                        if self.verbose_locals:
                            print("Found foreach local: "
                                      + f"{lcl_name} -> {lcl_vals}")
                    bracket_level += 1

            # =================================================================
            # Iterate over locals and see if something can be found
            # =================================================================
            for lpattern in self.patterns_local:
                pat = re.compile(lpattern)
                m = pat.search(line)
                if m is None:
                    continue
                local_name = m.group(1)
                # For locals, get a value
                if lpattern.find("local") != -1:
                    local_value = m.group(2)
                else:
                    local_value = ""

                # Tempfiles can list several local names, but all of them will
                # be without a value
                # tempfile a b c d e f -> 6 locals.
                if lpattern.find("tempfile") != -1:
                    local_value = ""
                    local_names = local_name.split(" ")
                    local_names = [x.strip() for x in local_names]
                    if "" in local_names:
                        local_names.remove("")
                else:
                    local_names = [local_name]

                # The iteration over lists is necessary because of tempfiles
                for local_name in local_names:
                    # print(f"{local_name} -> {local_value}")
                    local_value = self._replace_locals(local_value, local)
                    local_value = self.replace_globals(local_value)
                    local_value = self._replace_locals(local_value, local)
                    local_value = local_value.strip().strip("\"")
                    local[local_name] = local_value
                    if self.verbose_locals:
                        print("Found local %s -> %s" % (local_name,
                                                        local_value))
            # Check if the current line has a pattern that needs to be
            # excluded
            for pattern in self.patterns_exclude:
                pat = re.compile(pattern)
                m = pat.search(line)
                if m is None:
                    continue
                else:
                    """
                    print("Exclude pattern %s found in line %s"
                          % (pattern, line))
                    """
                    line = ""
                    break

            # Iterate over all patterns and try to find the best match
            # The best pattern is the most complex one (most capture groups)
            # and the one that fits the longest chunk of the code line
            best_pattern = None
            best_pattern_groups = -1
            best_pattern_len = -1
            best_pattern_type = None
            for pattern in self.patterns:
                m = re.search(pattern[0], line.strip())
                if m is None:
                    continue
                # Make sure that before the command, there are only
                # accepted patterns.
                line_pos = line.find(m.group(0))
                line_starts = line[:line_pos].strip()
                if line_starts != "":
                    if "quietly".startswith(line_starts):
                        pass
                    elif "noisily".startswith(line_starts):
                        pass
                    elif "capture".startswith(line_starts):
                        pass
                    elif "noisily".startswith(line_starts):
                        pass
                    elif line_starts.startswith("if "):
                        if line_starts.endswith("graph"):
                            if self.verbose_bef_pat:
                                print("Before pattern [if, graph]: "
                                      + f"{line_starts}")
                            continue
                        if self.verbose_bef_pat:
                            print("'if' line start [if, !graph]: "
                                  + f"{line_starts}")
                    else:
                        if self.verbose_bef_pat:
                            print(f"Before pattern [oth]: {line_starts}")
                        continue

                # Select the pattern with the most capture groups that also
                # covers most of the current code line.
                pattern_groups = len(m.groups())
                pattern_len = len(pattern[0])
                if (pattern_groups > best_pattern_groups or
                    (pattern_groups == best_pattern_groups
                     and pattern_len > best_pattern_len)):
                    best_pattern_len = pattern_len
                    best_pattern_groups = pattern_groups
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
                    if pat_str != "":
                        self.parsed[fname][i+1+(key-1)/100] \
                            = (pat_type, pat_str)

            i += 1

        if fname not in self.parsed:
            self.parsed[fname] = {}

        self._expand_parsed(local)

    def _max_key_by_floor(self, key_list, key_floor):
        max_key = -1
        for key in key_list:
            if math.floor(key) == key_floor:
                if key > max_key:
                    max_key = key
        return max_key

    def _expand_filename(self,
                         filename,
                         local={},
                         verbose=False):
        """
        Files of the form [[x|y|z]] were created by the expansion of locals
        from loops.

        local -> dictionary of locals, might be required for further expansion.
        """

        def _text_expand(element, local):
            if element.find("`") != -1 or element.find("'") != -1:
                element = self._replace_locals(element, local)
            return element

        files_new = []
        m = re.search("\\[\\[(.*?)\\]\\]", filename)
        if m:
            print(filename)
            if verbose:
                print(f"--> Pattern: {m.group(0)}")
            # Make sure that there was only one pattern in the local
            # TODO: If an error pops up, implement a better check.
            assert m.group(1).find("[[") == -1
            assert m.group(1).find("]]") == -1

            new_patterns = re.split("\\|", m.group(1))
            for new_pattern in new_patterns:
                file_new = filename.replace(m.group(0), new_pattern)
                files_new.append(file_new)

            if verbose:
                print("New files now:")
                print(files_new)

            # Recurse over files already processed to make sure no pattern
            # was missed
            files_new_rec = []
            for new_file in files_new:
                files_new2 = self._expand_filename(new_file)
                files_new_rec.extend(files_new2)
            return [_text_expand(x, local) for x in files_new_rec]
        else:
            return [_text_expand(filename, local)]

    def _expand_parsed(self, local):
        """
        Files of the form [[x|y|z]] were created by the expansion of locals
        from loops. This function does the post-processing of reverting
        this pattern back to a set of files.
        """
        for node in self.parsed.keys():

            entry_pop = []
            content_keys = list(self.parsed[node].keys())
            for entry in content_keys:
                action, file = self.parsed[node][entry]

                files_new = self._expand_filename(file, local=local)
                for file_new in files_new:
                    # Generate a new key at this level (maximum key + .001)
                    # Insert it into the list
                    max_key = self._max_key_by_floor(
                            self.parsed[node].keys(),
                            math.floor(entry))
                    assert max_key != -1
                    self.parsed[node][max_key + .001] = (action, file_new)

                # Mark the current entry for removal
                entry_pop.append(entry)

            # Remove all expanded entries
            for entry in entry_pop:
                self.parsed[node].pop(entry)

    def _replace_locals(self, s, local,
                        _rec_depth=0):
        """
        Replace locals in a string.

        local is a dictionary of local -> replacement combintions.
        """
        if _rec_depth > 10:
            print(f"Warning: High recursion depth on _replace_locals: {s}")
            return s
        if local is None:
            return s
        if s.find("`") == -1:
            return s
        s_prev = s
        for local_key in local.keys():
            local_from = "`" + local_key + "'"
            if s.find(local_from) != -1:
                local_to = local[local_key]

                """
                Handle cases where multiple options are available through loops
                """
                if type(local_to) is dict:
                    local_to = '|'.join(local_to['local_values'])
                    local_to = '[[' + local_to + ']]'

                """
                If a local is contained in the same local, this recursion can
                break the local replacement routine. This happens for example
                in loops in Stata code in the wild.
                """
                local_to = local_to.replace(local_from,
                                            "<removed recursive local>")
                s = s.replace(local_from, local_to)
        if s != s_prev:
            if self.verbose_locals:
                print("Replaced local: %s -> %s" % (s_prev, s))
            return self._replace_locals(s, local,
                                        _rec_depth=_rec_depth+1)
        else:
            return s

    def postproc_stata(self, fname, local=None):
        """
        Do postprocessing:
            - Replace \\ by /
            - Replace // by / (filenames)
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
        # Replace // by / (filenames)
        for i in sorted(self.parsed[fname].keys()):
            t = self.parsed[fname][i]
            self.parsed[fname][i] = (t[0], t[1].replace("\\\\", "/")
                                               .replace("\\", "/")
                                               .replace("\"", "")
                                               .replace("//", "/"))

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
                        print(f"Warning: File {t[1]} was used "
                              + "after being erased.")
                    elif j > i and t[0] == "tempfile":
                        self.parsed[fname].pop(j)
                    else:
                        self.parsed[fname].pop(j)
            # Delete the 'erase' instruction itself
            self.parsed[fname].pop(i)

    def _exp_get_do_node(self, fname):
        return self._exp_get_file_node("do", fname)

    def _ftype_to_color(self, ftype):
        if ftype == 'cluster':
            return "black"
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
        node = self._proc_node_name(fname)
        node_lbl = node.replace('/', '/\\n')
        color = self._ftype_to_color(ftype)
        fname_nonew = os.path.join(self.base_folder, fname.replace("\n", ""))
        return f"\"{node}\" [color={color}, URL=\"file:///{fname_nonew}\"," \
            + f" label=\"{node_lbl}\"]"

    def compile_graphviz(self,
                         in_filename,
                         out_filename,
                         view=True,
                         cleanup=True,
                         render_format='pdf'):
        """
        Cleanup: Remove the intermediate file and the input .viz file.
        """
        print("Compile graphviz content in %s" % in_filename)
        file_content = self._try_read_file(in_filename)
        file_content = "\n".join(file_content)

        src = Source(file_content)
        src.render(filename=out_filename + ".tmp",
                   outfile=out_filename,
                   view=view,
                   cleanup=cleanup,
                   format=render_format)

        if cleanup:
            os.remove(in_filename)
            # os.remove(out_filename)

        # If the output filename comes with the right file ending, remove it
        # and move the created file.
        # (Otherwise the output is out_filename.pdf.pdf)
        """
        if out_filename.endswith("." + render_format):
            shutil.move(out_filename + "." + render_format,
                        out_filename[:-len(render_format)-1])
        """

    def _proc_node_name(self, fname):
        """
        Format the node names as configured.
        """
        fname = fname.replace("\\", "/")
        fname = fname.replace(self.base_folder.replace("\\", "/"), "")
        if self.cut_paths:
            return os.path.split(fname)[1]
        else:
            return fname

    def export_table(self,
                     exclude_do=True):
        """
        Export for display as table.
        In the rows, individual (input/output) files are listed.
        In columns, .do files doing the input or output are listed.

        I: Initialized.
        D: Executed ('do').
        U: Use.
        S: Save.
        E: Export.

        Returns a pandas DataFrame.
        """

        # Auxiliary dictionary: Maps file name
        d_files = {}
        d_files_rev = {}
        for parsed_file in self.parsed.keys():
            fpath, fname = os.path.split(parsed_file)
            fname_use = fname
            i = 1
            while fname_use in d_files:
                i += 1
                fname_use = f"{fname} {i}"
            d_files[fname_use] = parsed_file
            d_files_rev[parsed_file] = fname_use

        # Output dictionary: file -> do-file -> action
        actions = {'init_file': {}}

        for fname in d_files.keys():
            actions['init_file'][fname] = 'I'

            to_process = self.parsed[d_files[fname]]

            for row, proc_entry in to_process.items():
                # Letter: U(se), S(ave), D(o), ...
                letter = proc_entry[0][0].upper()

                if exclude_do and letter == 'D':
                    continue

                proc_entry = proc_entry[1]

                if proc_entry not in actions:
                    actions[proc_entry] = {}

                if fname not in actions[proc_entry]:
                    actions[proc_entry][fname] = letter
                else:
                    actions[proc_entry][fname] += letter

        # Try to find an ordering of columns: Use topological sorting of
        # networkx
        g, l_in, l_out = self._execution_graph()

        # Check that no cycles are present
        if not nx.is_directed_acyclic_graph(g):
            cycles = nx.cycles.find_cycle(g)
            print("ERROR: Execution graph is not DAG!")
            print("Cycles:")
            for (f_in, f_out) in cycles:
                print(f"{f_in} -> {f_out}")
            raise AssertionError("Execution graph is not DAG")


        l_sorted = [d_files_rev[x] for x in nx.topological_sort(g)]

        actions = pd.DataFrame(actions).T
        actions = actions[l_sorted]
        actions = actions.sort_values(l_sorted, ascending=False)
        actions = actions[actions.index != 'init_file']

        return actions

    def export_graphviz(self, file,
                        separate_groups=False,
                        stack_clusters=2):
        """
        Export for graphical display

        separate_groups: If a file creates a number of files without
            subsequent usage, show them separately. Depending on the layout,
            they can otherwise take a lot of space.

        stack_clusters: Number of rows that grouped clusters should
            have. Default 2. Set to 'column' to only export one column.
        """
        if type(file) is str:
            f = open(file, "w+")
            f_opened = True
        else:
            f = file
            f_opened = False

        f.write("digraph StataReaderGraph {\n")
        f.write(self.indent + "graph [compound=true];\n")

        file_links = []
        file_nodes = []
        file_node_types = []
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
        # Add comment: Stata Code nodes start here
        f.write(self.indent + "/*\n")
        f.write(self.indent + self.indent + "Stata Code nodes\n")
        f.write(self.indent + "*/\n")
        # Define Stata Code node
        for fname in self.parsed:
            f.write(self.indent + self._exp_get_do_node(fname) + ";\n")
            fname_node = self._proc_node_name(fname)
            file_nodes.append(fname_node)
            file_node_types.append(".do")
        f.write("\n")

        # Add comment: Individual file nodes start here
        # First, find out which nodes are present. Also generate file links.
        # Since both lists may be modified by subsequent options, do not
        # write them out, yet
        for fname in self.parsed:
            fname_node = self._proc_node_name(fname)

            # Check if the node is to be disregarded.
            if fname_node in self.disregarded_nodes:
                continue

            for i in sorted(self.parsed[fname].keys()):
                t = self.parsed[fname][i]
                fname_node2 = self._proc_node_name(t[1])

                # Check if the node is to be disregarded.
                if fname_node2 in self.disregarded_nodes:
                    continue

                # If the node has not been written, do so now
                if t[1] not in file_nodes:
                    file_nodes.append(t[1])
                    file_node_types.append(t[0])
                    file_cluster_nodetypes[fname_node2] = t[0]

                # The type of action determines the direction of the arrow
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
                    file_cluster_usage[fname_node2] = []
                file_cluster_usage[fname_node2].append(fname_node)
        f.write("\n")

        """
        Determine which nodes need to be clustered together.
        This happens when nodes are only connected to a file. For clearer
        visibility, they should then be grouped.
        """
        """
        Write them out!
        """
        add_invis = []
        cluster_names = []
        cluster_idx = 0
        for cluster_type in file_clusters.keys():
            # Identify possible clusters
            groups = {}
            for node in file_clusters[cluster_type].keys():
                node_connections = file_clusters[cluster_type][node]
                # Only create a cluster if the number of nodes interacting
                # with a file is one.
                if len(node_connections) == 1:
                    file_for_node = node_connections[0]
                    if file_for_node not in groups:
                        groups[file_for_node] = []
                    if len(set(file_cluster_usage[node])) == 1:
                        if node not in file_cluster_nodetypes:
                            print(f" >>> Error: {node} not contained")
                            print(file_cluster_nodetypes)
                        if file_cluster_nodetypes[node] == cluster_type:
                            groups[file_for_node].append(node)

            # Show clusters separately in the graph
            for cluster in groups:
                if len(groups[cluster]) > 1:

                    # Determine cluster type, name derives from it
                    # Clusters with .dta files should never be grouped
                    # together
                    ext = os.path.splitext(groups[cluster][0])
                    if ext[1] == "":
                        cluster_name = f"Cluster {cluster_idx}"
                    else:
                        cluster_name = "Cluster %d\n(%d %s files)" \
                            % (cluster_idx, len(groups[cluster]), ext[1])
                    cluster_idx += 1

                    if separate_groups:
                        # Add a new replacement node
                        if ext[1] != "":
                            file_nodes.append(cluster_name)
                            file_node_types.append("cluster")
                            cluster_names.append(cluster_name)

                        # Go through every element contained in the cluster
                        # and replace it everywhere by a new name
                        # This concerns especially file links
                        for element in groups[cluster]:
                            if ext[1] == "":
                                continue
                            for i in range(len(file_links)):
                                if file_links[i][0] == element:
                                    file_links[i] = (cluster_name,
                                                     file_links[i][1])
                                if file_links[i][1] == element:
                                    file_links[i] = (file_links[i][0],
                                                     cluster_name)

                    f.write("subgraph \"cluster_%s_%s\" {\n"
                            % (cluster.replace(".", "_"), cluster_type))
                    if separate_groups:
                        f.write(self.indent
                                + 'label = "'
                                + cluster_name.replace("\n", " ")
                                + " -> file %s" % cluster_type
                                + '";\n')
                        f.write(self.indent + 'labeljust = "l";\n')
                    f.write(self.indent + 'shape=rect;\n')
                    f.write(self.indent + "rank = same;\n")
                    for element in groups[cluster]:
                        f.write(self.indent + "\"%s\";\n" % element)

                    # Add hidden edges to give some internal structure to
                    # the cluster
                    if stack_clusters == 'column':
                        stack_clusters = 999
                    idx = 0
                    while (idx < len(groups[cluster])):
                        for i in range(stack_clusters-1):
                            if idx+1 < len(groups[cluster]):
                                add_invis.append('"%s" -> "%s" %s;\n'
                                                 % (groups[cluster][idx],
                                                    groups[cluster][idx+1],
                                                    "[style=invis]"))

                                # Remove external link to the internally linked
                                # ones
                                idx_fl = 0
                                while idx_fl < len(file_links):
                                    if file_links[idx_fl][1] \
                                            == groups[cluster][idx+1]:
                                        file_links.pop(idx_fl)
                                        continue
                                    if file_links[idx_fl][0] \
                                            == groups[cluster][idx]:
                                        file_links.pop(idx_fl)
                                        continue
                                    idx_fl += 1
                            else:
                                break
                            idx += 1
                        idx += 1

                    f.write(self.indent + "graph[style=dotted];\n")
                    f.write("}\n")

        # Order clusters
        """
        TODO: More space-efficient display of the clusters?
        idx1 = 0
        idx2 = 1
        add_invis.append('"%s" -> "%s" [style=invis];\n'
                         % (cluster_names[idx1],
                            cluster_names[idx2]))
        """

        """
        Write the input/output nodes into the output file
        """
        f.write(self.indent + "/*\n")
        f.write(self.indent + self.indent + "Input / Output file nodes\n")
        f.write(self.indent + "*/\n")
        for i in range(len(file_nodes)):
            if file_node_types[i] == ".do":
                continue
            f.write(self.indent
                    + self._exp_get_file_node(file_node_types[i],
                                              file_nodes[i]) + ";\n")

        # Add comment: Input / Output relationships start here
        f.write(self.indent + "/*\n")
        f.write(self.indent + self.indent + "Input/Output relationships\n")
        f.write(self.indent + "*/\n")
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

            fname_node2 = self._proc_node_name(t[1])

            if has_backward is False:
                f.write(self.indent
                        + "\"%s\" -> \"%s\"\n" % (link[0], link[1]))
            else:
                f.write(self.indent
                        + "\"%s\" -> \"%s\" [dir=\"both\"]\n"
                        % (link[0], link[1]))

            i += 1

        """
        Write out invisible edges
        """
        for invis in add_invis:
            f.write(self.indent + invis)

        f.write("}\n")
        if f_opened:
            f.close()

    def read_folder(self,
                    folder,
                    exclude=[],
                    walk=False,
                    as_master=False,
                    set_base_folder='if_null'):
        """
        Read a directory and parse all .do files that are encountered.

        exclude: Ignore files with these names.
        walk: read subdirs as well.
        as_master: Instead of calling read_stata, call read_stata_master.

        set_base_folder: Set the base folder. Default: Set it only if it was
            not set at initialization. Put 'True' if it should always be set.
        """
        for file in os.scandir(folder):
            file_name = str(file.name)
            if file_name in exclude:
                print(f"Excluded file: '{file_name}'")
                continue
            fext = os.path.splitext(file_name)[1]
            if file.is_file() and fext == ".do":
                print(f"Reading Stata file '{file_name}'")
                if not as_master:
                    self.read_stata(os.path.join(folder, file_name))
                else:
                    self.read_stata_master(os.path.join(folder, file_name))
            elif file.is_file() and self.header_patterns is not None:
                if fext in self.header_patterns['filetypes']:
                    self.read_header(os.path.join(folder, file_name))
            elif file.is_dir() and walk:
                self.read_folder(os.path.join(folder, file_name),
                                 walk=True,
                                 exclude=exclude)
            else:
                pass
                # print(f"Unknown file: '{file_name}'")

        # This needs to be at the end to set it at the last recursion.
        if set_base_folder == "if_null":
            if self.base_folder == "":
                self.base_folder = folder
        elif set_base_folder is True:
            self.base_folder = folder

    def get_dta_files(self):
        """
        Return a list of all possible dta-files involved in this project.
        Also return which file used them.
        """
        dta_files = {}
        for file in self.parsed.keys():
            file_content = self.parsed[file]
            for node_key in file_content.keys():
                node = file_content[node_key]
                if node[0] in ['use', 'save']:
                    if node[1] in dta_files:
                        if node[1] not in dta_files[node[1]]:
                            dta_files[node[1]].append(file)
                    else:
                        dta_files[node[1]] = [file]
        return dta_files

    def _execution_graph(self):
        """
        Auxiliary method doing the heavy lifting for create_master_file.
        """
        g = nx.DiGraph()
        file_nodes = {}

        # Go through linkages within the scanned code base.
        # For every data file, save the file that creates it and all the files
        # that use it.
        # In the final graph, nodes will be Stata code files.
        for node in self.parsed.keys():

            # Do not process further if the file is to be disregarded.
            if node in self.disregarded_nodes:
                continue

            if node not in g.nodes:
                g.add_node(node)

            content = self.parsed[node]
            for entry in content.keys():
                action, file = content[entry]

                # IF a file directly executes another file, ignore it for now.
                if action == 'do':
                    continue

                if file in self.disregarded_nodes:
                    print(f"Warning: Disregarded node {file}")
                    continue

                if file not in file_nodes:
                    file_nodes[file] = {
                            'creator': None,
                            'users': []
                            }

                # External usage
                if action in ['use', 'use_ext']:
                    # If the file itself is already set as creator, then
                    # the file is allowed to use the output without creating
                    # a loop.
                    # Without this check, there would be cycles in script:
                    # save A.dta
                    # use A.dta
                    # save B.dta
                    if node != file_nodes[file]['creator']:
                        file_nodes[file]['users'].append(node)
                    else:
                        print(f"Info: Node {node} saves and uses file {file}")
                # Saving / Exporting
                elif action in ['save', 'export']:
                    if file_nodes[file]['creator'] is not None:
                        if file_nodes[file]['creator'] != node:
                            print(f"ERROR: creator of {file} already set!")
                    file_nodes[file]['creator'] = node
                # Not implemented error
                else:
                    raise ValueError(f"Unknown file action {action}")

        # Input files are such that are not created by any file.
        # Directed links are created between Stata code files creating a
        # data files and Stata code files using the file.
        input_files = []
        # Output files are such that are instead created at any point during
        # the execution.
        output_files = []
        for file in file_nodes.keys():
            content = file_nodes[file]

            if content['creator'] is None:
                if file not in input_files:
                    input_files.append(file.replace("\\", "/"))
                continue
            else:
                if file not in output_files:
                    output_files.append(file.replace("\\", "/"))

            for user in content['users']:
                g.add_edge(content['creator'], user)

        # Make sure that input and output files do not overlap
        # (Should mechanically be true)
        s_if = set(input_files)
        s_of = set(output_files)
        s_ovl = s_if.intersection(s_of)
        if len(s_ovl) != 0:
            print("Warning: Overlap of input/output files detected.")
            for f in s_ovl:
                print(f"    Overlapping file: {f}")

        return g, input_files, output_files

    def create_master_file(self):
        """
        Create master.do file.
        Return list of Stata lines detailing:
            - Input files (as comments in the first rows)
            - Proposed execution order for code files.
            - Output files (as comments in the last rows)
        The method will fail if cyclical execution patterns are present in the
        code base.
        """
        g, input_files, output_files = self._execution_graph()

        # Check that no cycles are present
        if not nx.is_directed_acyclic_graph(g):
            cycles = nx.cycles.find_cycle(g)
            print("ERROR: Execution graph is not DAG!")
            print("Cycles:")
            for (f_in, f_out) in cycles:
                print(f"{f_in} -> {f_out}")
            raise AssertionError("Execution graph is not DAG")

        # Create the output: First, detected input files. Then, proposed
        # execution order.
        master_do = []
        for input_file in sorted(input_files):
            master_do.append(f"// Requires input file {input_file}\n")
        for node in nx.topological_sort(g):
            node = node.replace("\\", "/")
            master_do.append(f'do "{node}"\n')
        for output_file in sorted(output_files):
            master_do.append(f"// Creates output file {output_file}\n")
        return master_do
