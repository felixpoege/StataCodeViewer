# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:10:06 2020

@author: poef
"""
import sys
sys.path.append("../")
from StataReader import StataReader

PATH = "C:/Dropbox/NPL_Papers/Submissions/Science/Replication/do/"
PATH_OUT = "Z:/Eigene Dateien/Projekte/2018_DAG/"

reader = StataReader()
reader.parse_global_file(PATH + "main.do")
reader.read_folder(PATH,
                   exclude=["create_freeze_data.do",
                            "main.do"])

reader.export_graphviz(PATH_OUT + "ScienceQuality.viz",
                       separate_groups=False,
                       stack_clusters='column')
reader.compile_graphviz(PATH_OUT + "ScienceQuality.viz",
                        PATH_OUT + "ScienceQuality.pdf")
