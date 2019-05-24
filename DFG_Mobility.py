# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:06:42 2019

@author: Poef
"""

import os
# import subprocess
from StataReader import StataReader

PATH_OUT = "Z:\\Eigene Dateien\\Projekte\\2018_DAG\\"
PATH_DO = "C:/Dropbox/DFG_Mobility/3_PROJECTS/P.1_sudden deaths/analysis/prog/"
PATH_DOT = "C:/Program Files (x86)/Graphviz2.38/bin/dot.exe"

reader = StataReader()
reader.parse_global_file(PATH_DO + "master.do")
for file in ["1_3_preprocess_patents",
             "1_4_inventor_productivity_panel",
             "1_5_network_dynamics",
             "2_1_deceased_inventors",
             "2_2_deceased_inventors_netw",
             "2_3_prepare_match",
             "2_4_execute_match",
             "2_6_prepare_teamtenure",
             "2_6_prepare_teamtenure_IAB",
             "2_6_prepare_teamtenure_patents",
             "2_7_mobility",
             "2_10_productivity_focal",
             "3_1_describe_match",
             "3_2_regressions"]:
    reader.read_stata(PATH_DO + file + ".do",
                      local={'folder': ''})

# reader.set_verbose_locals(True)
reader.read_stata(PATH_DO + "2_5_prepare_regressions" + ".do",
                      local={'data_type': 'dead'}
                      )
with open(PATH_OUT + "mobility.viz", "w+") as f:
    reader.export_graphviz(f)
cmd = "\"%s\" -Tpng \"%s\" > \"%s\"" % (PATH_DOT,
                                        PATH_OUT + "mobility.viz",
                                        PATH_OUT + "mobility.png")
o = os.popen(cmd).read()

