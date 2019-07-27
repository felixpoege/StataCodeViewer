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

PATH = r"X:\Prof. Harhoff\Harhoff_INTERN\FORSCHUNG\NPL\\"
PATH_OUT = "Z:/Eigene Dateien/Projekte/2018_DAG/"
PATH_DOT = "C:/Program Files (x86)/Graphviz2.38/bin/dot.exe"

reader = StataReader()

reader.disregard_node("NPL_paths.do")
reader.disregard_node("clean_expand_query.do")

reader.parse_global_file(PATH + "NPL_paths.do")
reader.read_folder(PATH + r"Conferences_npl/do/")
reader.read_folder(PATH + r"do/conf_spons/",
                   exclude=['master.do'])
reader.read_folder(PATH + r"do/conf_spons/describe/")

"""
reader.parse_global_file(PATH
                         + r"do/conf_spons/estimation/Manski77_master.do")
"""
"""
reader.read_stata(PATH + r"do/conf_spons/build_scopus_citation_counts.do")
reader.read_stata(PATH + r"do/conf_spons/describe/Descriptives.do")
reader.read_stata(PATH
                  + r"do/conf_spons/test_build_conf_similarity_scores.do")
reader.read_stata(PATH
+ r"do/conf_spons/estimation/describe_citation_counts.do")
# reader.read_stata(PATH + r"do/conf_spons/estimation/Manski77_prepare.do")
"""
"""
reader.read_stata(PATH + r"do/conf_spons/Geocoding/prepare_geocoding.do")
reader.read_stata(PATH + r"do/conf_spons/Geocoding/"
                  + "finalize_conference_geocoding.do")
reader.read_stata(PATH + r"do/conf_spons/Geocoding//"
                  + "build_company_applicant_portfolios.do")
reader.read_stata(PATH + r"do/conf_spons/Geocoding/"
                  + "build_company_inventor_portfolios.do")
"""
reader.read_folder(PATH + r"do/conf_spons/Geocoding/")
with open(PATH_OUT + "conferences.viz", "w") as f:
    reader.export_graphviz(f)

cmd = "\"%s\" -Tpng \"%s\" > \"%s\"" % (PATH_DOT,
                                        PATH_OUT + "conferences.viz",
                                        PATH_OUT + "conferences.png")
o = os.popen(cmd).read()

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
