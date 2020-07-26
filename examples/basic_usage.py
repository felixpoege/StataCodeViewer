# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:57:20 2020

@author: Poef
"""
import sys
sys.path.append("../")
from StataReader import StataReader

reader = StataReader()

reader.read_folder("stata_example/")

# These files will not be shown in the flowchart.
# Use this for files that are used very often or are irrelevant.
ignore_nodes = ["ignore.do", "ignore.dta"]
for node in ignore_nodes:
    reader.disregard_node(node)

# Create the flowchart
reader.export_graphviz("flowchart.viz")
reader.compile_graphviz("flowchart.viz",
                        "flowchart",
                        render_format='png')
