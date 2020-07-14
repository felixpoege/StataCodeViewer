# StataCodeViewer

Visualize flows of Stata code

Which .do file

* Uses which data source

* Creates which files

Global and Local processing is very ad-hoc, so this works best for relatively simple and linear scripts (as many Stata projects tend to be ...)

## Installation / Usage

(The package is very much work in process, please let me know of any difficulty)

You'll need Python to run the script.

* Download the repository from GitHub, for example by downloading the ZIP file. Extract it to a location of your choice.
* Install the required libraries (graphviz following https://pypi.org/project/graphviz/)
* Set up a script to analyze your Stata code. Follow the examples in the example/ folder or the example below.

## Example

Put this Code to the same folder as the other examples.

```python
import sys
sys.path.append("../")
from StataReader import StataReader

reader = StataReader()

# Include all files from your project
for file in os.scandir("/path/to/your/Stata/folder/"):
    reader.read_stata(file)

# These files will not be shown in the flowchart.
# Use this for files that are used very often or are irrelevant.
ignore_nodes = ["ignore.do", "ignore.dta"]
for node in ignore_nodes:
    reader.disregard_node(node)

# Create the flowchart
reader.export_graphviz("flowchart.viz")
reader.compile_graphviz(flowchart.viz", "flowchart")
```
