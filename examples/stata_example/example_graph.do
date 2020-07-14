/*
	Create some simple output files based on the example data
*/
use "example_auto.dta", clear

// First, a graph
twoway (scatter price mpg)
graph export "scatter.png", replace

// Second, a table
reg price mpg, robust
esttab . using "regression.tex", tex replace
