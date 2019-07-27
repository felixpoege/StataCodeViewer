/*
	Utility file which extracts documentation-relevant information from Stata documents
*/
args folder file output_file

assert !missing("`file'")
assert !missing("`folder'")
assert !missing("`output_file'")

di "Debug: file=`file'"
di "Debug: folder=`folder'"
di "Debug: output_file=`output_file'"

if substr("`folder'", -1, 1) != "/" {
	local folder = "`folder'/"
}

/*if "`file'" 

local files = `" "conf_spon/persons.dta" "conf_spon\scientist_experience.dta" "conf_spon\scientist_experience_paperlevel.dta" "conf_spon\biographies.dta" "'
local folders = `" "${DATA_MAIN}" "${DATA_MAIN}" "${DATA_MAIN}" "${DATA_MAIN}""'
*/
cap log close _all

quietly {
	log using "`output_file'", replace

	noi di as result "Dataset documentation: `file'"
	noi di as text "{hline}"
	noi di as text "Containing folder: `folder'"
	use in 1 using "`folder'`file'", clear
	noi describe using "`folder'`file'" 
	noi notes list
	
	noi di as text _n _n

	log close _all
}
