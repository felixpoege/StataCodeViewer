# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:41:41 2019

@author: Poef
"""

import sys
import os
sys.path.append("../")
from StataReader import StataReader

PATH = r"X:\Prof. Harhoff\Harhoff_INTERN\FORSCHUNG\NPL\\"
PATH_OUT = "Z:/Eigene Dateien/Projekte/2018_DAG/"
PATH_DOT = "C:/Program Files (x86)/Graphviz2.38/bin/dot.exe"

reader = StataReader()

reader.disregard_node("NPL_paths.do")
reader.parse_global_file(PATH + "NPL_paths.do")
# reader.read_folder(PATH + r"do/mpdl_method_paper/")
reader.read_folder(PATH + r"do/mpdl_method_paper/regressions/")
# reader.read_folder(PATH + r"do/mpdl_method_paper/descriptives/")
# reader.read_folder(PATH + r"do/mpdl_method_paper/data/")

with open(PATH_OUT + "SNPL.viz", "w") as f:
    reader.export_graphviz(f)

cmd = "\"%s\" -Tpng \"%s\" > \"%s\"" % (PATH_DOT,
                                        PATH_OUT + "SNPL.viz",
                                        PATH_OUT + "SNPL.png")
o = os.popen(cmd).read()
print(o)
