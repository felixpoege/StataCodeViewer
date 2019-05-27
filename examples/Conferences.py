# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:41:41 2019

@author: Poef
"""

PATH = r"X:\Prof. Harhoff\Harhoff_INTERN\FORSCHUNG\NPL\\"
reader = StataReader()

reader.disregard_node("NPL_paths.do")
reader.disregard_node("clean_expand_query.do")

# Test 1: Three files
reader.read_stata(PATH
                  + r"Conferences_npl/do/read_conference_items_wos.do")
reader.read_stata(PATH
                  + r"Conferences_npl/do/read_conference_items_scopus.do")
reader.read_stata(PATH + r"do/conf_spons/describe/desc_full_sample.do")
reader.parse_global_file(PATH + "NPL_paths.do")
reader.parse_global_file(PATH
                         + r"do/conf_spons/estimation/Manski77_master.do")
reader.read_stata(PATH + r"do/conf_spons/build_conf_final.do")
reader.read_stata(PATH + r"do/conf_spons/build_conf_final_locations.do")
"""
reader.read_stata(PATH + r"do/conf_spons/build_scopus_citation_counts.do")
reader.read_stata(PATH + r"do/conf_spons/describe/Descriptives.do")
reader.read_stata(PATH
                  + r"do/conf_spons/test_build_conf_similarity_scores.do")
reader.read_stata(PATH
+ r"do/conf_spons/estimation/describe_citation_counts.do")
# reader.read_stata(PATH + r"do/conf_spons/estimation/Manski77_prepare.do")
"""
reader.read_stata(PATH + r"do/conf_spons/Geocoding/prepare_geocoding.do")
reader.read_stata(PATH + r"do/conf_spons/Geocoding/"
                  + "finalize_conference_geocoding.do")
reader.read_stata(PATH + r"do/conf_spons/Geocoding//"
                  + "build_company_applicant_portfolios.do")
reader.read_stata(PATH + r"do/conf_spons/Geocoding/"
                  + "build_company_inventor_portfolios.do")

reader.export_graphviz(sys.stdout)