# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:41:41 2019

@author: Poef
"""

import sys
import os
import hashlib
sys.path.append("../")
from StataReader import StataReader

PATH = "X:/Prof. Harhoff/Harhoff_INTERN/RESEARCH/NPL/"
PATH_OUT = "Z:/Eigene Dateien/Projekte/2018_DAG/"

"""
Create flow chart for the data construction files
"""
files = ["read_bvd_id_components",
         "build_conf_participant_aff",
         "build_conf_final",
         "build_biographies",
         "compute_similarity",
         "build_cooperations",
         "build_previous_participation",
         "build_conf_citation_counts",
         "estimation_matching/regs_second_stage"]

files_mainreg = [
        "estimation_matching/matching_1_conf_level",
        "estimation_matching/matching_2_geolocation",
        "estimation_matching/matching_3_first_stage",
        "estimation_matching/matching_4_auxiliaries",
        "estimation_matching/matching_5_second_stage",
        "estimation_matching/balancing_table",
        "flows/flows_build_dataset",
        "flows/flows_did_analysis",
        "flows/plot_flows_did_analysis"]

files_descriptives = [
        "scoreboard_panel/match_grid_orbis",
        "scoreboard_panel/describe_companies",
        "scoreboard_panel/describe_companies_table",
        "scoreboard_panel/describe_scoreboard",
        "describe/describe_citation_counts",
        "describe/desc_full_sample",
        "describe/describe_coauthorships",
        "describe/describe_count",
        "describe/describe_sample_coverage",
        "describe/Descriptives",
        "describe/table_core_fields"]

nodes_disregard = [
        "NPL_paths.do",
        "settings.do",
        "clean_expand_query.do",
        "generate_conf_part_vars.do",
        "concatenate_var.do"]

"""
Create graph for the main analysis
"""
reader = StataReader()
for node in nodes_disregard:
    reader.disregard_node(node)
reader.parse_global_file(PATH + "NPL_paths.do")

for file in files:
    reader.read_stata(PATH + "do/conf_spons/" + file + ".do")
for file in files_mainreg:
    reader.read_stata(PATH + "do/conf_spons/" + file + ".do")

reader.export_graphviz(PATH_OUT + "conferences_mainreg.viz",
                       separate_groups=True,
                       stack_clusters=5)
reader.compile_graphviz(PATH_OUT + "conferences_mainreg.viz",
                        PATH_OUT + "conferences_mainreg")

"""
Create graph for descriptives and supplementary analysis
"""
reader = StataReader()
for node in nodes_disregard:
    reader.disregard_node(node)
reader.parse_global_file(PATH + "NPL_paths.do")

for file in files:
    reader.read_stata(PATH + "do/conf_spons/" + file + ".do")
for file in files_descriptives:
    reader.read_stata(PATH + "do/conf_spons/" + file + ".do")

reader.export_graphviz(PATH_OUT + "conferences_descriptives.viz",
                       separate_groups=True,
                       stack_clusters=5)
reader.compile_graphviz(PATH_OUT + "conferences_descriptives.viz",
                        PATH_OUT + "conferences_descriptives")

xxxxxxx
"""
Automatically create documentation files concerning Stata file contents
"""
PATH_STATA = "C:/Program Files (x86)/Stata15/StataSE-64.exe"

# Retreive all data files involved in the project
dta_files = reader.get_dta_files()


def get_documentation(PATH_STATA, path, file,
                      use_cache=True):
    """
    Use a Stata program to retreive documentation information from the
    .dta file <file>.
    """
    if not os.path.exists("tmp_logs"):
        os.mkdir("tmp_logs")

    h = hashlib.new('sha256')
    fname = "%s%s" % (path, file)
    h.update(fname.encode())
    log_file = "tmp_logs/" + h.hexdigest() + ".log"

    if os.path.exists(log_file) and use_cache:
        print("Loaded from storage.")
        with open(log_file, "r") as f:
            doc = f.readlines()
        return doc
    else:
        cmd_line = "\"%s\" -e ../create_documentation.do \"%s\" \"%s\" \"%s\""
        p = os.popen(cmd_line % (PATH_STATA, path, file, log_file)).read()
        if p.strip() != "":
            print(p)
        with open("out_file.log", "r") as f:
            doc = f.readlines()
        return doc


# Create documentation for all of them by using Stata
logs = {}
n_keys = len(dta_files.keys())
c_key = 0
for dta_file in dta_files.keys():
    c_key += 1
    path, file = os.path.split(dta_file)
    file = file.strip()
    print("%d/%d: %s" % (c_key, n_keys, file))

    if os.path.exists(os.path.join(path, file)):
        log = get_documentation(PATH_STATA, path, file)
    elif os.path.exists(os.path.join(path, file + ".dta")):
        log = get_documentation(PATH_STATA, path, file + ".dta")
    else:
        print("Not found.")
        log = ["NOT FOUND"]

    # Bring lines that are too long to the previous line
    i = 0
    while i < len(log):
        line = log[i]
        if line.startswith("> "):
            log[i-1] = log[i-1][:-1] + log.pop(i)[2:]
        else:
            i += 1

    logs[dta_file] = log

# Put all the logs into a separate document
markdown_doc = ["Documentation"]
markdown_doc.append("=============")
for dta_file in logs.keys():
    path, file = os.path.split(dta_file)
    file = file.strip()

    markdown_doc.append(file)
    markdown_doc.append("".join(["-" for x in range(len(file))]))

    if len(logs[dta_file]) == 1 and logs[dta_file][0] == "NOT FOUND":
        markdown_doc.append("Containing folder: %s" % path)
        markdown_doc.append("")

    markdown_doc.extend([x.rstrip("\n") for x in logs[dta_file]])
    markdown_doc.append("")
    markdown_doc.append("")

# Take care of malformed file names
markdown_doc = [x.replace("//", "/") for x in markdown_doc]

with open("documentation.md", "w") as f:
    f.write("\n".join(markdown_doc))
