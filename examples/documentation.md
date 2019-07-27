Documentation
=============
wos_conferences_participants_with_city
--------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_GENERAL/WoS/DATA/conferences

NOT FOUND


wos_conferences_participants_only_IDs
-------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_GENERAL/WoS/DATA/conferences

NOT FOUND


sco_conf_proceeding_date
------------------------
Dataset documentation: sco_conf_proceeding_date.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:     5,949,838                          5 Jan 2018 14:32
 vars:             7                          
 size:   136,846,274                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %10.0g                
proceed_year    int     %10.0g                
proceed_month   byte    %10.0g                
proceed_day     byte    %10.0g                
proceed_year_first
                int     %10.0g                
proceed_year_last
                int     %10.0g                
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_event_date
-------------------
Dataset documentation: sco_conf_event_date.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:     5,920,866                          13 Jan 2018 14:16
 vars:             8                          
 size:   136,179,918                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %10.0g                
event_start_year
                int     %10.0g                conf_start YEAR
event_start_month
                byte    %10.0g                conf_start MONTH
event_start_day byte    %10.0g                conf_start DAY
event_end_year  int     %10.0g                conf_end YEAR
event_end_month byte    %10.0g                conf_end MONTH
event_end_day   byte    %10.0g                conf_end DAY
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_addresses
------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep

NOT FOUND


sco_conf_titles
---------------
Dataset documentation: sco_conf_titles.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:     5,949,838                          5 Jan 2018 14:31
 vars:             3                          
 size:   136,846,274 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %12.0g                
title           strL    %9s                   
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_items_and_classification
---------------------------------
Dataset documentation: sco_conf_items_and_classification.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:    12,500,488                          5 Jan 2018 11:39
 vars:             5                          
 size:   525,020,496                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %10.0g                
pk_items        double  %10.0g                
item_id         str18   %18s                  
document_type   str2    %9s                   
ASJC            int     %10.0g                
-------------------------------------------------------------------------------
Sorted by: 





ASJC
----
Dataset documentation: ASJC.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/Scopus/Classifications/

Contains data                                 
  obs:           334                          1 Dec 2017 01:37
 vars:             8                          
 size:        48,430                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
ASJC_Top        str17   %17s                  ASJC_Top
ASJC_Middle     str44   %44s                  ASJC_Middle
ASJC_Low        str60   %60s                  ASJC_Low
ASJC            int     %10.0g                ASJC
oecd_main       byte    %10.0g                oecd_main
oecd_code       byte    %10.0g                oecd_code
oecd_main_name  str3    %9s                   oecd_main_name
oecd_nameshort  str13   %13s                  oecd_nameshort
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_subj_weights
---------------------
Dataset documentation: sco_conf_subj_weights.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:     5,949,711                          5 Jan 2018 14:30
 vars:            27                          
 size: 1,237,539,888                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %10.0g                
weightBAUSTELLE double  %10.0g                (sum) weightBAUSTELLE
weightagr_agro  double  %10.0g                (sum) weightagr_agro
weightagr_animal
                byte    %10.0g                (sum) weightagr_animal
weightagr_veter double  %10.0g                (sum) weightagr_veter
weighteng_civil double  %10.0g                (sum) weighteng_civil
weighteng_environ
                double  %10.0g                (sum) weighteng_environ
weighteng_materials
                double  %10.0g                (sum) weighteng_materials
weighteng_mechan
                double  %10.0g                (sum) weighteng_mechan
weighteng_other double  %10.0g                (sum) weighteng_other
weightmed_basic double  %10.0g                (sum) weightmed_basic
weightmed_health
                double  %10.0g                (sum) weightmed_health
weightnnn       double  %10.0g                (sum) weightnnn
weightsci_chem  double  %10.0g                (sum) weightsci_chem
weightsci_infosci
                double  %10.0g                (sum) weightsci_infosci
weightsci_mathem
                double  %10.0g                (sum) weightsci_mathem
weightsoc_econ  double  %10.0g                (sum) weightsoc_econ
weightsoc_law   double  %10.0g                (sum) weightsoc_law
weightsoc_psychol
                double  %10.0g                (sum) weightsoc_psychol
weightAgriculture
                double  %10.0g                (sum) weightAgriculture
weightEngineering
                double  %10.0g                (sum) weightEngineering
weightHumanities
                double  %10.0g                (sum) weightHumanities
weightMedicine  double  %10.0g                (sum) weightMedicine
weightNot_known double  %10.0g                (sum) weightNot_known
weightScience   double  %10.0g                (sum) weightScience
weightSocial_Science
                double  %10.0g                (sum) weightSocial_Science
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: pk_conferences  





sponsor_cleaning_table
----------------------
Dataset documentation: sponsor_cleaning_table.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/

Contains data                                 
  obs:       207,369                          17 Jan 2018 15:41
 vars:             2                          
 size:   106,172,928                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
sponsor         str254  %254s                 
sponsors_clean  str254  %254s                 
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_sponsors
-----------------
Dataset documentation: sco_conf_sponsors.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:     8,899,551                          23 Jan 2018 10:46
 vars:             3                          
 size: 2,393,979,219                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %10.0g                
sponsor         str254  %254s                 
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_itemlist
-----------------
Dataset documentation: wos_conf_itemlist.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          9 Jan 2018 09:29
 vars:             2                          
 size:   118,712,448                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
fk_items        long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_addresses
------------------
Dataset documentation: wos_conf_addresses.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          9 Jan 2018 09:33
 vars:             5                          
 size:   643,025,760 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
host            strL    %9s                   
city            str26   %26s                  
state           str20   %20s                  
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_titles
---------------
Dataset documentation: wos_conf_titles.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          9 Jan 2018 09:35
 vars:             3                          
 size:   187,961,376 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
title           strL    %9s                   
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_itemlist
-----------------
Dataset documentation: wos_conf_itemlist.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          9 Jan 2018 09:29
 vars:             2                          
 size:   118,712,448                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
fk_items        long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_proceeding_date
------------------------
Dataset documentation: wos_conf_proceeding_date.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     1,795,682                          9 Jan 2018 09:41
 vars:             5                          
 size:    34,117,958                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
fk_sources      long    %8.0g                 
pubmonth        byte    %10.0g                
pubyear         int     %8.0g                 
fk_items        long    %12.0g                
pk_conferences  long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_event_date_full
------------------------
Dataset documentation: wos_conf_event_date_full.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,703                          9 Jan 2018 09:46
 vars:             8                          
 size:   484,742,447                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
event_start_date
                long    %10.0g                
event_end_date  long    %10.0g                
event_start_year
                int     %10.0g                
event_start_month
                byte    %10.0g                
event_end_year  int     %10.0g                
event_end_month byte    %10.0g                
event_date      str27   %27s                  
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_event_date
-------------------
Dataset documentation: wos_conf_event_date.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,703                          9 Jan 2018 09:46
 vars:             6                          
 size:   168,175,951                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
event_start_year
                int     %10.0g                
event_start_month
                byte    %10.0g                
event_end_year  int     %10.0g                
event_end_month byte    %10.0g                
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





OECD_subj_codes
---------------
Dataset documentation: OECD_subj_codes.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl/

Contains data                                 
  obs:            39                          19 Dec 2017 15:28
 vars:             4                          
 size:         3,822                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
subj_oecd_main  byte    %8.0g                 SUBJ_OECD_MAIN
subj_oecd_code  double  %10.0g                SUBJ_OECD_CODE
subj_oecd_namefull
                str71   %71s                  SUBJ_OECD_NAMEFULL
subj_oecd_nameshort
                str14   %14s                  SUBJ_OECD_NAMESHORT
-------------------------------------------------------------------------------
Sorted by: subj_oecd_code  





wos_conf_items_subj_weight
--------------------------
Dataset documentation: wos_conf_items_subj_weight.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          9 Jan 2018 11:51
 vars:            50                          
 size: 3,868,047,264                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
fk_items        long    %12.0g                
weightagr_agro  double  %10.0g                agr_agro weight
weightagr_animal
                double  %10.0g                agr_animal weight
weightagr_other double  %10.0g                agr_other weight
weightagr_veter double  %10.0g                agr_veter weight
weighteng_biotech
                double  %10.0g                eng_biotech weight
weighteng_chem  double  %10.0g                eng_chem weight
weighteng_civil double  %10.0g                eng_civil weight
weighteng_electr
                double  %10.0g                eng_electr weight
weighteng_environ
                double  %10.0g                eng_environ weight
weighteng_indbiotech
                double  %10.0g                eng_indbiotech weight
weighteng_material
                double  %10.0g                eng_material weight
weighteng_mechan
                double  %10.0g                eng_mechan weight
weighteng_medical
                double  %10.0g                eng_medical weight
weighteng_other double  %10.0g                eng_other weight
weighthum_arts  double  %10.0g                hum_arts weight
weighthum_history
                double  %10.0g                hum_history weight
weighthum_language
                double  %10.0g                hum_language weight
weighthum_other double  %10.0g                hum_other weight
weighthum_philos
                double  %10.0g                hum_philos weight
weightmed_basic double  %10.0g                med_basic weight
weightmed_clin  double  %10.0g                med_clin weight
weightmed_health
                double  %10.0g                med_health weight
weightnnn       double  %10.0g                nnn weight
weightsci_biol  double  %10.0g                sci_biol weight
weightsci_chem  double  %10.0g                sci_chem weight
weightsci_environ
                double  %10.0g                sci_environ weight
weightsci_infosci
                double  %10.0g                sci_infosci weight
weightsci_mathem
                double  %10.0g                sci_mathem weight
weightsci_other double  %10.0g                sci_other weight
weightsci_physics
                double  %10.0g                sci_physics weight
weightsoc_commun
                double  %10.0g                soc_commun weight
weightsoc_econ  double  %10.0g                soc_econ weight
weightsoc_educ  double  %10.0g                soc_educ weight
weightsoc_geogr double  %10.0g                soc_geogr weight
weightsoc_law   double  %10.0g                soc_law weight
weightsoc_other double  %10.0g                soc_other weight
weightsoc_politics
                double  %10.0g                soc_politics weight
weightsoc_psychol
                double  %10.0g                soc_psychol weight
weightsoc_sociol
                double  %10.0g                soc_sociol weight
weightAgriculture
                double  %10.0g                Agriculture weight
weightEngineering
                double  %10.0g                Engineering weight
weightHumanities
                double  %10.0g                Humanities weight
weightMedicine  double  %10.0g                Medicine weight
weightNot_known double  %10.0g                Not_known weight
weightScience   double  %10.0g                Science weight
weightSocial_Science
                double  %10.0g                Social_Science weight
pk_conferences  long    %12.0g                
weightUnknown   double  %10.0g                
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_subj_weights
---------------------
Dataset documentation: wos_conf_subj_weights.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          14 Jan 2018 17:19
 vars:            49                          
 size: 3,828,476,448                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
weightagr_agro  double  %10.0g                (sum) weightagr_agro
weightagr_animal
                double  %10.0g                (sum) weightagr_animal
weightagr_other double  %10.0g                (sum) weightagr_other
weightagr_veter double  %10.0g                (sum) weightagr_veter
weighteng_biotech
                double  %10.0g                (sum) weighteng_biotech
weighteng_chem  double  %10.0g                (sum) weighteng_chem
weighteng_civil double  %10.0g                (sum) weighteng_civil
weighteng_electr
                double  %10.0g                (sum) weighteng_electr
weighteng_environ
                double  %10.0g                (sum) weighteng_environ
weighteng_indbiotech
                double  %10.0g                (sum) weighteng_indbiotech
weighteng_material
                double  %10.0g                (sum) weighteng_material
weighteng_mechan
                double  %10.0g                (sum) weighteng_mechan
weighteng_medical
                double  %10.0g                (sum) weighteng_medical
weighteng_other double  %10.0g                (sum) weighteng_other
weighthum_arts  double  %10.0g                (sum) weighthum_arts
weighthum_history
                double  %10.0g                (sum) weighthum_history
weighthum_language
                double  %10.0g                (sum) weighthum_language
weighthum_other double  %10.0g                (sum) weighthum_other
weighthum_philos
                double  %10.0g                (sum) weighthum_philos
weightmed_basic double  %10.0g                (sum) weightmed_basic
weightmed_clin  double  %10.0g                (sum) weightmed_clin
weightmed_health
                double  %10.0g                (sum) weightmed_health
weightnnn       double  %10.0g                (sum) weightnnn
weightsci_biol  double  %10.0g                (sum) weightsci_biol
weightsci_chem  double  %10.0g                (sum) weightsci_chem
weightsci_environ
                double  %10.0g                (sum) weightsci_environ
weightsci_infosci
                double  %10.0g                (sum) weightsci_infosci
weightsci_mathem
                double  %10.0g                (sum) weightsci_mathem
weightsci_other double  %10.0g                (sum) weightsci_other
weightsci_physics
                double  %10.0g                (sum) weightsci_physics
weightsoc_commun
                double  %10.0g                (sum) weightsoc_commun
weightsoc_econ  double  %10.0g                (sum) weightsoc_econ
weightsoc_educ  double  %10.0g                (sum) weightsoc_educ
weightsoc_geogr double  %10.0g                (sum) weightsoc_geogr
weightsoc_law   double  %10.0g                (sum) weightsoc_law
weightsoc_other double  %10.0g                (sum) weightsoc_other
weightsoc_politics
                double  %10.0g                (sum) weightsoc_politics
weightsoc_psychol
                double  %10.0g                (sum) weightsoc_psychol
weightsoc_sociol
                double  %10.0g                (sum) weightsoc_sociol
weightAgriculture
                double  %10.0g                (sum) weightAgriculture
weightEngineering
                double  %10.0g                (sum) weightEngineering
weightHumanities
                double  %10.0g                (sum) weightHumanities
weightMedicine  double  %10.0g                (sum) weightMedicine
weightNot_known double  %10.0g                (sum) weightNot_known
weightScience   double  %10.0g                (sum) weightScience
weightSocial_Science
                double  %10.0g                (sum) weightSocial_Science
weightUnknown   double  %10.0g                (sum) weightUnknown
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: pk_conferences  





wos_sponsors_clean
------------------
Dataset documentation: wos_sponsors_clean.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:    27,827,395                          23 Jan 2018 10:41
 vars:             3                          
 size: 4,675,002,360                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
sponsor         str157  %157s                 
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_item_to_pk_conferences
-------------------------------
Dataset documentation: sco_conf_item_to_pk_conferences.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:     5,949,838                          4 Jul 2018 10:14
 vars:             2                          
 size:   178,495,140                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %10.0g                
id              str18   %18s                  
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_affiliation_locations
------------------------------
Dataset documentation: sco_conf_affiliation_locations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:    14,683,143                          5 Mar 2018 14:21
 vars:             6                          
 size:11,952,078,402                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_affiliations double  %10.0g                
country_code    str3    %9s                   
country         str1    %9s                   
text            str625  %625s                 
address_part    str113  %113s                 
city_group      str60   %60s                  
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_affiliations
---------------------
Dataset documentation: sco_conf_affiliations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:     4,510,966                          6 Jan 2018 01:22
 vars:             2                          
 size: 1,312,691,106                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_affiliations double  %10.0g                
query           str279  %279s                 
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_items
--------------
Dataset documentation: wos_conf_items.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          4 Jul 2018 11:01
 vars:             3                          
 size:   306,673,824                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_items        long    %12.0g                
id              str19   %19s                  
pk_conferences  long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_item_to_pk_conferences
-------------------------------
Dataset documentation: wos_conf_item_to_pk_conferences.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:     9,892,704                          4 Jul 2018 11:03
 vars:             2                          
 size:   267,103,008                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id              str19   %19s                  
pk_conferences  long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





wos_pk_conferences_to_pk_addresses
----------------------------------
Dataset documentation: wos_pk_conferences_to_pk_addresses.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:    20,609,124                          2 Nov 2018 13:21
 vars:             2                          
 size:   247,309,488                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  long    %12.0g                
pk_addresses    long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





wos_conf_affiliations
---------------------
Dataset documentation: wos_conf_affiliations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/wos_prep/

Contains data                                 
  obs:    15,294,045                          12 Jan 2018 13:41
 vars:             2                          
 size: 1,835,285,400                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_addresses    long    %12.0g                
query           str112  %112s                 
-------------------------------------------------------------------------------
Sorted by: 





country_state_translation_table
-------------------------------
Dataset documentation: country_state_translation_table.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/

Contains data                                 
  obs:         1,266                          14 Jan 2018 17:58
 vars:             4                          
 size:       116,472                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
old_state       str24   %24s                  old_state
old_country     str20   %20s                  old_country
new_state       str24   %24s                  new_state
new_country     str20   %20s                  new_country
-------------------------------------------------------------------------------
Sorted by: 





conferences_combined_full
-------------------------
Dataset documentation: conferences_combined_full.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/

Contains data                                 
  obs:    15,842,542                          14 Jan 2018 17:59
 vars:            70                          
 size: 8,158,909,130 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %12.0g                
title           strL    %9s                   
conf_type       str3    %9s                   
event_start_year
                int     %10.0g                conf_start YEAR
event_start_month
                byte    %10.0g                conf_start MONTH
event_end_year  int     %10.0g                conf_end YEAR
event_end_month byte    %10.0g                conf_end MONTH
proceed_year    int     %10.0g                
proceed_month   byte    %10.0g                
proceed_day     byte    %10.0g                
proceed_year_first
                int     %10.0g                
proceed_year_last
                int     %10.0g                
event_start_day byte    %10.0g                conf_start DAY
event_end_day   byte    %10.0g                conf_end DAY
postalcode      strL    %9s                   
address_part    strL    %9s                   
city            strL    %9s                   
venue           strL    %9s                   
host            strL    %9s                   
weightagr_agro  double  %10.0g                (sum) weightagr_agro
weightagr_animal
                double  %10.0g                (sum) weightagr_animal
weightagr_other double  %10.0g                (sum) weightagr_other
weightagr_veter double  %10.0g                (sum) weightagr_veter
weighteng_biotech
                double  %10.0g                (sum) weighteng_biotech
weighteng_chem  double  %10.0g                (sum) weighteng_chem
weighteng_civil double  %10.0g                (sum) weighteng_civil
weighteng_electr
                double  %10.0g                (sum) weighteng_electr
weighteng_environ
                double  %10.0g                (sum) weighteng_environ
weighteng_indbiotech
                double  %10.0g                (sum) weighteng_indbiotech
weighteng_material
                double  %10.0g                (sum) weighteng_material
weighteng_mechan
                double  %10.0g                (sum) weighteng_mechan
weighteng_medical
                double  %10.0g                (sum) weighteng_medical
weighteng_other double  %10.0g                (sum) weighteng_other
weighthum_arts  double  %10.0g                (sum) weighthum_arts
weighthum_history
                double  %10.0g                (sum) weighthum_history
weighthum_language
                double  %10.0g                (sum) weighthum_language
weighthum_other double  %10.0g                (sum) weighthum_other
weighthum_philos
                double  %10.0g                (sum) weighthum_philos
weightmed_basic double  %10.0g                (sum) weightmed_basic
weightmed_clin  double  %10.0g                (sum) weightmed_clin
weightmed_health
                double  %10.0g                (sum) weightmed_health
weightnnn       double  %10.0g                (sum) weightnnn
weightsci_biol  double  %10.0g                (sum) weightsci_biol
weightsci_chem  double  %10.0g                (sum) weightsci_chem
weightsci_environ
                double  %10.0g                (sum) weightsci_environ
weightsci_infosci
                double  %10.0g                (sum) weightsci_infosci
weightsci_mathem
                double  %10.0g                (sum) weightsci_mathem
weightsci_other double  %10.0g                (sum) weightsci_other
weightsci_physics
                double  %10.0g                (sum) weightsci_physics
weightsoc_commun
                double  %10.0g                (sum) weightsoc_commun
weightsoc_econ  double  %10.0g                (sum) weightsoc_econ
weightsoc_educ  double  %10.0g                (sum) weightsoc_educ
weightsoc_geogr double  %10.0g                (sum) weightsoc_geogr
weightsoc_law   double  %10.0g                (sum) weightsoc_law
weightsoc_other double  %10.0g                (sum) weightsoc_other
weightsoc_politics
                double  %10.0g                (sum) weightsoc_politics
weightsoc_psychol
                double  %10.0g                (sum) weightsoc_psychol
weightsoc_sociol
                double  %10.0g                (sum) weightsoc_sociol
weightAgriculture
                double  %10.0g                (sum) weightAgriculture
weightEngineering
                double  %10.0g                (sum) weightEngineering
weightHumanities
                double  %10.0g                (sum) weightHumanities
weightMedicine  double  %10.0g                (sum) weightMedicine
weightNot_known double  %10.0g                (sum) weightNot_known
weightScience   double  %10.0g                (sum) weightScience
weightSocial_Science
                double  %10.0g                (sum) weightSocial_Science
weightUnknown   double  %10.0g                (sum) weightUnknown
weightBAUSTELLE double  %10.0g                (sum) weightBAUSTELLE
weighteng_materials
                double  %10.0g                (sum) weighteng_materials
state           str24   %24s                  new_state
country         str20   %20s                  new_country
-------------------------------------------------------------------------------
Sorted by: 





conferences_pk_conferences_to_conf_event_id
-------------------------------------------
Dataset documentation: conferences_pk_conferences_to_conf_event_id.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/

Contains data                                 
  obs:    15,842,542                          14 Jan 2018 18:02
 vars:             3                          
 size:   301,008,298                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %12.0g                
conf_type       str3    %9s                   
conf_event_id   float   %9.0g                 group(title event_start_year
                                                proceed_year state country)
-------------------------------------------------------------------------------
Sorted by: 





conferences_combined_small
--------------------------
Dataset documentation: conferences_combined_small.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/

Contains data                                 
  obs:       304,752                          14 Jan 2018 18:10
 vars:            15                          
 size:    39,922,512 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
conf_event_id   float   %9.0g                 group(title event_start_year
                                                proceed_year state country)
conf_type       str3    %9s                   (first) conf_type
title           strL    %9s                   (first) title
event_start_year
                int     %10.0g                (first) event_start_year
proceed_year    int     %10.0g                (first) proceed_year
country         str20   %20s                  (first) country
state           str24   %24s                  (first) state
weightsci_infosci
                double  %10.0g                (sum) weightsci_infosci
weightAgriculture
                double  %10.0g                (sum) weightAgriculture
weightEngineering
                double  %10.0g                (sum) weightEngineering
weightHumanities
                double  %10.0g                (sum) weightHumanities
weightMedicine  double  %10.0g                (sum) weightMedicine
weightNot_known double  %10.0g                (sum) weightNot_known
weightScience   double  %10.0g                (sum) weightScience
weightSocial_Science
                double  %10.0g                (sum) weightSocial_Science
-------------------------------------------------------------------------------
Sorted by: conf_event_id  





dblp_only_year
--------------
Dataset documentation: dblp_only_year.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     3,501,504                          11 Mar 2019 17:17
 vars:             2                          
 size:   241,603,776                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
year            int     %10.0g                
-------------------------------------------------------------------------------
Sorted by: 





persons
-------
Dataset documentation: persons.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Person-Paper dataset
  obs:     9,789,793                          24 Jul 2019 18:43
 vars:             5                          
 size: 1,272,673,090                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
personname      str57   %57s                  
order           int     %8.0g                 
n_persons       int     %8.0g                 
year            int     %10.0g                
-------------------------------------------------------------------------------
Sorted by: 

_dta:
  1.  "persontype is restricted to author (no editors ...)"
  2.  "year is restricted to 1990 and later"
  3.  "Creation date 24 Jul 2019 18:42 "
  4.  "Creation file build_biographies.do"





conf_final
----------
Dataset documentation: conf_final.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     1,864,229                          11 Mar 2019 17:16
 vars:            18                          
 size:   467,921,479 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str62   %62s                  
crosref         str33   %33s                  
year            int     %8.0g                 start_year
city_clean      str31   %31s                  city_clean
lat_city        float   %9.0g                 
lon_city        float   %9.0g                 
country_code    str2    %9s                   country_code
conf_dblp_id    str21   %21s                  conf_dblp_id
id_event        str60   %60s                  Unique ID for a conference event
has_scowos_data byte    %9.0g                 
core_field_1    int     %8.0g                 1 core_field_
core_field_2    int     %8.0g                 2 core_field_
core_field_3    int     %8.0g                 3 core_field_
core_rank       str2    %9s                   
has_CORE        byte    %9.0g                 
sponsor_component
                strL    %9s                   
participant_components
                strL    %9s                   
conference_items_N
                int     %9.0g                 Number of conference items
-------------------------------------------------------------------------------
Sorted by: id_event  key_resource  





dblp_citation_counts
--------------------
Dataset documentation: dblp_citation_counts.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Within-DBLP citation links
                                                based on Scopus citation links
  obs:     2,796,338                          27 Jul 2018 15:37
 vars:            24                          
 size:   315,986,194                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  DBLP item which received the
                                                citation
cited_year      int     %10.0g                DBLP publication year of the
                                                cited item
count_within_1  int     %9.0g                 # citing year - cited year <= 1
                                                (in DBLP)
count_within_2  int     %9.0g                 # citing year - cited year <= 2
                                                (in DBLP)
count_within_3  int     %9.0g                 # citing year - cited year <= 3
                                                (in DBLP)
count_within_4  int     %9.0g                 # citing year - cited year <= 4
                                                (in DBLP)
count_within_5  int     %9.0g                 # citing year - cited year <= 5
                                                (in DBLP)
count_within_6  int     %9.0g                 # citing year - cited year <= 6
                                                (in DBLP)
count_within_7  int     %9.0g                 # citing year - cited year <= 7
                                                (in DBLP)
count_within_8  int     %9.0g                 # citing year - cited year <= 8
                                                (in DBLP)
count_within_9  int     %9.0g                 # citing year - cited year <= 9
                                                (in DBLP)
count_within_10 int     %9.0g                 # citing year - cited year <= 10
                                                (in DBLP)
count_within_11 int     %9.0g                 # citing year - cited year <= 11
                                                (in DBLP)
count_within_12 int     %9.0g                 # citing year - cited year <= 12
                                                (in DBLP)
count_within_13 int     %9.0g                 # citing year - cited year <= 13
                                                (in DBLP)
count_within_14 int     %9.0g                 # citing year - cited year <= 14
                                                (in DBLP)
count_within_15 int     %9.0g                 # citing year - cited year <= 15
                                                (in DBLP)
count_within_16 int     %9.0g                 # citing year - cited year <= 16
                                                (in DBLP)
count_within_17 int     %9.0g                 # citing year - cited year <= 17
                                                (in DBLP)
count_within_18 int     %9.0g                 # citing year - cited year <= 18
                                                (in DBLP)
count_within_19 int     %9.0g                 # citing year - cited year <= 19
                                                (in DBLP)
count_within_20 int     %9.0g                 # citing year - cited year <= 20
                                                (in DBLP)
count_within_ever
                int     %9.0g                 # Cited ever (in DBLP)
count_within_scowos
                int     %9.0g                 # Cited ever (in Scopus/WoS)
-------------------------------------------------------------------------------
Sorted by: key_resource  





scientist_experience
--------------------
Dataset documentation: scientist_experience.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Scientist-level # papers/cites
                                                of past (EXCLUDING current!) 5
                                                years/ever (NOTES)
  obs:     7,675,606                          24 Jul 2019 23:33
 vars:            22                          
 size:   790,587,418                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
personname      str57   %57s                  
year            int     %10.0g                
exp_count_cumul_A
                int     %9.0g                 Scientist: Count articles
                                                (lifetime) A conferences
exp_cit5_cumul_A
                int     %9.0g                 Scientist: Count citations
                                                (lifetime) A conferences
exp_count_cumul_As
                int     %9.0g                 Scientist: Count articles
                                                (lifetime) A* conferences
exp_cit5_cumul_As
                int     %9.0g                 Scientist: Count citations
                                                (lifetime) A* conferences
exp_count_cumul_no_conf
                int     %9.0g                 Scientist: Count articles
                                                (lifetime) A*-D conferences
exp_cit5_cumul_no_conf
                int     %9.0g                 Scientist: Count citations
                                                (lifetime) A*-D conferences
exp_cit5_w5_A   int     %9.0g                 Scientist: Count citations (last
                                                5y) A conferences
exp_cit5_w5_As  int     %9.0g                 Scientist: Count citations (last
                                                5y) A* conferences
exp_cit5_w5_no_conf
                int     %9.0g                 Scientist: Count citations (last
                                                5y) A*-D conferences
exp_count_w5_A  int     %9.0g                 Scientist: Count articles (last
                                                5y) A conferences
exp_count_w5_As int     %9.0g                 Scientist: Count articles (last
                                                5y) A* conferences
exp_count_w5_no_conf
                int     %9.0g                 Scientist: Count articles (last
                                                5y) A*-D conferences
exp_count_cumul_conf
                int     %9.0g                 Scientist: Count articles
                                                (lifetime) A*-D conferences
exp_cit5_cumul_conf
                int     %9.0g                 Scientist: Count citations
                                                (lifetime) A*-D conferences
exp_count_w5_conf
                int     %9.0g                 Scientist: Count articles (last
                                                5y) A*-D conferences
exp_cit5_w5_conf
                int     %9.0g                 Scientist: Count citations (last
                                                5y) A*-D conferences
exp_count_cumul_all
                int     %9.0g                 Scientist: Count articles
                                                (lifetime) all types
exp_cit5_cumul_all
                int     %9.0g                 Scientist: Count citations
                                                (lifetime) all types
exp_count_w5_all
                int     %9.0g                 Scientist: Count articles (last
                                                5y) all types
exp_cit5_w5_all int     %9.0g                 Scientist: Count citations (last
                                                5y) all types
-------------------------------------------------------------------------------
Sorted by: personname  year  

_dta:
  1.  "The dataset contains only the years the scientists were actually active
      in (+ the year later, often). This is because having the full name-year
      list would be too large ..."
  2.  "The count for 2000 would include a sum of the years 1995-1999"
  3.  "Divide citation count by article count for averages (obviously)"
  4.  "all: conferences with CORE-ranking + unknown conferences +
      non-conference articles"
  5.  "conf: conferences with CORE-ranking"
  6.  "no_conf: non-conference articles (journals, books)"
  7.  "Creation date 24 Jul 2019 23:33 "
  8.  "Creation file build_biographies.do"





scientist_experience_paperlevel
-------------------------------
Dataset documentation: scientist_experience_paperlevel.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Paper-level # papers/cites of
                                                past (EXCLUDING current!) 5
                                                years/ever (NOTES)
  obs:     3,322,180                          25 Jul 2019 12:13
 vars:            41                          
 size:   621,247,660                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
exp_count_cumul_A
                float   %9.0g                 All Authors: Count articles
                                                (lifetime) A conferences
exp_cit5_cumul_A
                float   %9.0g                 All Authors: Count citations
                                                (lifetime) A conferences
exp_count_cumul_As
                float   %9.0g                 All Authors: Count articles
                                                (lifetime) A* conferences
exp_cit5_cumul_As
                float   %9.0g                 All Authors: Count citations
                                                (lifetime) A* conferences
exp_count_cumul_no_conf
                float   %9.0g                 All Authors: Count articles
                                                (lifetime) A*-D conferences
exp_cit5_cumul_no_conf
                float   %9.0g                 All Authors: Count citations
                                                (lifetime) A*-D conferences
exp_cit5_w5_A   float   %9.0g                 All Authors: Count citations
                                                (last 5y) A conferences
exp_cit5_w5_As  float   %9.0g                 All Authors: Count citations
                                                (last 5y) A* conferences
exp_cit5_w5_no_conf
                float   %9.0g                 All Authors: Count citations
                                                (last 5y) A*-D conferences
exp_count_w5_A  float   %9.0g                 All Authors: Count articles (last
                                                5y) A conferences
exp_count_w5_As float   %9.0g                 All Authors: Count articles (last
                                                5y) A* conferences
exp_count_w5_no_conf
                float   %9.0g                 All Authors: Count articles (last
                                                5y) A*-D conferences
exp_count_cumul_conf
                float   %9.0g                 All Authors: Count articles
                                                (lifetime) A*-D conferences
exp_cit5_cumul_conf
                float   %9.0g                 All Authors: Count citations
                                                (lifetime) A*-D conferences
exp_count_w5_conf
                float   %9.0g                 All Authors: Count articles (last
                                                5y) A*-D conferences
exp_cit5_w5_conf
                float   %9.0g                 All Authors: Count citations
                                                (last 5y) A*-D conferences
exp_count_cumul_all
                float   %9.0g                 All Authors: Count articles
                                                (lifetime) all types
exp_cit5_cumul_all
                float   %9.0g                 All Authors: Count citations
                                                (lifetime) all types
exp_count_w5_all
                float   %9.0g                 All Authors: Count articles (last
                                                5y) all types
exp_cit5_w5_all float   %9.0g                 All Authors: Count citations
                                                (last 5y) all types
exp_count_cumul_A_first
                int     %9.0g                 First Author: Count articles
                                                (lifetime) A conferences
exp_cit5_cumul_A_first
                int     %9.0g                 First Author: Count citations
                                                (lifetime) A conferences
exp_count_cumul_As_first
                int     %9.0g                 First Author: Count articles
                                                (lifetime) A* conferences
exp_cit5_cumul_As_first
                int     %9.0g                 First Author: Count citations
                                                (lifetime) A* conferences
exp_count_cumul_no_conf_first
                int     %9.0g                 First Author: Count articles
                                                (lifetime) A*-D conferences
exp_cit5_cumul_no_conf_first
                int     %9.0g                 First Author: Count citations
                                                (lifetime) A*-D conferences
exp_cit5_w5_A_first
                int     %9.0g                 First Author: Count citations
                                                (last 5y) A conferences
exp_cit5_w5_As_first
                int     %9.0g                 First Author: Count citations
                                                (last 5y) A* conferences
exp_cit5_w5_no_conf_first
                int     %9.0g                 First Author: Count citations
                                                (last 5y) A*-D conferences
exp_count_w5_A_first
                int     %9.0g                 First Author: Count articles
                                                (last 5y) A conferences
exp_count_w5_As_first
                int     %9.0g                 First Author: Count articles
                                                (last 5y) A* conferences
exp_count_w5_no_conf_first
                int     %9.0g                 First Author: Count articles
                                                (last 5y) A*-D conferences
exp_count_cumul_conf_first
                int     %9.0g                 First Author: Count articles
                                                (lifetime) A*-D conferences
exp_cit5_cumul_conf_first
                int     %9.0g                 First Author: Count citations
                                                (lifetime) A*-D conferences
exp_count_w5_conf_first
                int     %9.0g                 First Author: Count articles
                                                (last 5y) A*-D conferences
exp_cit5_w5_conf_first
                int     %9.0g                 First Author: Count citations
                                                (last 5y) A*-D conferences
exp_count_cumul_all_first
                int     %9.0g                 First Author: Count articles
                                                (lifetime) all types
exp_cit5_cumul_all_first
                int     %9.0g                 First Author: Count citations
                                                (lifetime) all types
exp_count_w5_all_first
                int     %9.0g                 First Author: Count articles
                                                (last 5y) all types
exp_cit5_w5_all_first
                int     %9.0g                 First Author: Count citations
                                                (last 5y) all types
-------------------------------------------------------------------------------
Sorted by: key_resource  

_dta:
  1.  "Variabels for mean of all authors / first author values exist"
  2.  "Divide citation count by article count for averages (actually only
      really works for first-author values ...)"
  3.  "all: conferences with CORE-ranking + unknown conferences +
      non-conference articles"
  4.  "conf: conferences with CORE-ranking"
  5.  "no_conf: non-conference articles (journals, books)"
  6.  "Creation date 25 Jul 2019 12:12 "
  7.  "Creation file build_biographies.do"





conf_persons
------------
Dataset documentation: conf_persons.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     3,387,030                          12 May 2019 20:15
 vars:             2                          
 size:   419,991,720                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
personname      str57   %57s                  
-------------------------------------------------------------------------------
Sorted by: 





dblp_scowos_match
-----------------
Dataset documentation: dblp_scowos_match.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/

Contains data                                 
  obs:     2,796,338                          13 Jul 2018 14:53
 vars:            10                          
 size:   503,340,840                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
dblp_type       str13   %13s                  
id1             str19   %19s                  1 id
id2             str19   %19s                  2 id
id3             str19   %19s                  3 id
id4             str19   %19s                  4 id
type_match1     str6    %9s                   1 type_match
type_match2     str6    %9s                   2 type_match
type_match3     str6    %9s                   3 type_match
type_match4     str6    %9s                   4 type_match
-------------------------------------------------------------------------------
Sorted by: key_resource  





sco_dblp_items_conf_affiliations_clean
--------------------------------------
Dataset documentation: sco_dblp_items_conf_affiliations_clean.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/dblp_match/

Contains data                                 
  obs:     2,274,656                          25 Jul 2018 00:32
 vars:             8                          
 size: 1,041,792,448                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id              str18   %18s                  
sequence_nr     int     %10.0g                
fk_persons      double  %10.0g                
pk_affiliations double  %10.0g                
country_code    str94   %94s                  
city_group      str60   %60s                  
person_type     byte    %14.0g     ptype      
query           str263  %263s                 
-------------------------------------------------------------------------------
Sorted by: 





wos_dblp_items_conf_affiliations_clean
--------------------------------------
Dataset documentation: wos_dblp_items_conf_affiliations_clean.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/dblp_match/

Contains data                                 
  obs:     2,945,569                          25 Jul 2018 01:00
 vars:             5                          
 size:   471,291,040                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
query           str127  %127s                 
pk_addresses    long    %8.0g                 
pk_items        long    %8.0g                 
addr_number     int     %8.0g                 
id              str19   %19s                  
-------------------------------------------------------------------------------
Sorted by: 





cluster_all_final
-----------------
Dataset documentation: cluster_all_final.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/final/

Contains data                                 
  obs:     1,518,899                          11 Mar 2019 15:25
 vars:             2                          
 size:   435,924,013                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
query           str235  %235s                 
company_name    str48   %48s                  
-------------------------------------------------------------------------------
Sorted by: query  





biographies
-----------
Dataset documentation: biographies.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     2,938,078                          18 Mar 2019 14:11
 vars:             6                          
 size:   390,764,374                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
company_name    str48   %48s                  
personname      str57   %57s                  
year            float   %10.0g                
weight_known    double  %9.0g                 (sum) weight
weight_ipolate  double  %10.0g                
weight_stay     float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: personname  company_name  year  





wos_dblp_items_conf_affiliations_clean
--------------------------------------
Dataset documentation: wos_dblp_items_conf_affiliations_clean.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/dblp_match/

Contains data                                 
  obs:     2,945,569                          25 Jul 2018 01:00
 vars:             5                          
 size:   471,291,040                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
query           str127  %127s                 
pk_addresses    long    %8.0g                 
pk_items        long    %8.0g                 
addr_number     int     %8.0g                 
id              str19   %19s                  
-------------------------------------------------------------------------------
Sorted by: 





sco_dblp_items_conf_affiliations_clean
--------------------------------------
Dataset documentation: sco_dblp_items_conf_affiliations_clean.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/dblp_match/

Contains data                                 
  obs:     2,274,656                          25 Jul 2018 00:32
 vars:             8                          
 size: 1,041,792,448                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id              str18   %18s                  
sequence_nr     int     %10.0g                
fk_persons      double  %10.0g                
pk_affiliations double  %10.0g                
country_code    str94   %94s                  
city_group      str60   %60s                  
person_type     byte    %14.0g     ptype      
query           str263  %263s                 
-------------------------------------------------------------------------------
Sorted by: 





cluster_orbis_confpart
----------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/final

NOT FOUND


company_info_publications
-------------------------
Dataset documentation: company_info_publications.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:       153,474                          28 Feb 2018 17:21
 vars:             5                          
 size:    19,644,672                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
year            str10   %10s                  
dblp_type       str13   %13s                  
id              str19   %19s                  ID
bvd_id_number   str19   %19s                  
-------------------------------------------------------------------------------
Sorted by: 





tmp_itemcounts
--------------
Dataset documentation: tmp_itemcounts.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:        33,072                          7 Dec 2018 15:31
 vars:             2                          
 size:     1,620,528                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
crosref         str37   %37s                  
count_items     double  %9.0g                 (sum) count_items
-------------------------------------------------------------------------------
Sorted by: crosref  





tmp_conf_series_clean
---------------------
Dataset documentation: tmp_conf_series_clean.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:        27,278                          11 May 2018 16:07
 vars:             7                          
 size:     4,991,874                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
crosref         str33   %33s                  crosref
conf_dblp_id    str21   %21s                  conf_dblp_id
year            int     %10.0g                year
city            str39   %39s                  city
country         str22   %22s                  country
country_code    str2    %9s                   country_code
id_event        str60   %60s                  
-------------------------------------------------------------------------------
Sorted by: 





dblp_asjc_weights
-----------------
Dataset documentation: dblp_asjc_weights.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 ASJC classifications for DBLP
                                                items as determined by
                                                Scopus+WoS items
  obs:     8,442,311                          11 May 2018 15:38
 vars:             3                          
 size:   650,057,947                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
asjc            int     %10.0g                All Journal Science
                                                Classification
weight_asjc     double  %9.0g                 Contribution based on WoS,
                                                Scopus, DBLP match
-------------------------------------------------------------------------------
Sorted by: key_resource  asjc  





ASJC_aggregation
----------------
Dataset documentation: ASJC_aggregation.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Translation from ASJC codes to
                                                aggregated ASJC codes (w >=
                                                0.001 share of DBLP)
  obs:           296                          11 May 2018 17:09
 vars:             2                          
 size:        14,800                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
asjc            int     %10.0g                All Journal Science
                                                Classification
asjc_agg        str44   %44s                  All Journal Science
                                                Classification (Aggregated)
-------------------------------------------------------------------------------
Sorted by: 





npl_person_names
----------------
Dataset documentation: npl_person_names.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/query_sources/

Contains data                                 
  obs:     2,139,239                          6 Jun 2018 22:38
 vars:             6                          
 size: 1,180,859,928                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
person_id       long    %12.0g                
han_id          long    %12.0g                
person_name     str253  %253s                 
person_ctry_code
                str2    %9s                   
han_name        str252  %252s                 
psn_sector      str33   %33s                  
-------------------------------------------------------------------------------
Sorted by: 





person_id_to_appln_id
---------------------
Dataset documentation: person_id_to_appln_id.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:    28,248,772                          11 Mar 2019 16:45
 vars:             4                          
 size:   564,975,440                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
person_id       long    %12.0g                
han_id          long    %12.0g                
pat_publn_id    long    %12.0g                
appln_id        long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





PATSTAT_basic_042017
--------------------
Containing folder: E:/PATSTAT/2017-04/DTA

NOT FOUND


company_patents
---------------
Dataset documentation: company_patents.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 List of all patents that
                                                npl-citing companies applied
                                                for, by HAN_ID.
  obs:    20,962,432                          11 Mar 2019 16:47
 vars:            10                          
 size: 2,662,228,864                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
person_id       long    %12.0g                
pat_publn_id    long    %12.0g                
appln_id        long    %12.0g                
person_name_component
                str48   %48s                  
han_name_component
                str48   %48s                  
docdb_family_id long    %12.0g                id for DOCDB family (long)
earliest_filing_date
                long    %d                    earliest filing date
area35          int     %22.0g     arealab35
                                              technological area (TF35)
mainarea35      byte    %11.0g     mainlab35
                                              main techn. area (TF35)
priority_year   float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: 

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





tls211
------
Containing folder: E:/PATSTAT/2017-04/DTA

NOT FOUND


concordance_dblp_area35_sco_classifications
-------------------------------------------
Dataset documentation: concordance_dblp_area35_sco_classifications.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:         3,122                          11 Mar 2019 16:51
 vars:             3                          
 size:        49,952                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
area35          int     %22.0g     arealab35
                                              technological area (TF35)
asjc            int     %10.0g                All Journal Science
                                                Classification
factor_area35   double  %9.0g                 Factor area35 -> ASJC
-------------------------------------------------------------------------------
Sorted by: area35  asjc  

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





concordance_dblp_mainarea35_sco_classifications
-----------------------------------------------
Dataset documentation: concordance_dblp_mainarea35_sco_classifications.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:           715                          11 Mar 2019 16:51
 vars:             3                          
 size:        10,725                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
mainarea35      byte    %11.0g     mainlab35
                                              main techn. area (TF35)
asjc            int     %10.0g                All Journal Science
                                                Classification
factor_mainarea35
                double  %9.0g                 Factor mainarea35 -> ASJC
-------------------------------------------------------------------------------
Sorted by: mainarea35  asjc  

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





npl_nplpubln_personid
---------------------
Dataset documentation: npl_nplpubln_personid.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/query_sources/

Contains data                                 
  obs:     5,394,636                          6 Jun 2018 22:28
 vars:             6                          
 size:   124,076,628                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
appln_id        long    %12.0g                
pat_publn_id    long    %12.0g                
applt_seq_nr    byte    %8.0g                 
person_id       long    %12.0g                
han_id          long    %12.0g                
publn_date      int     %td                   
-------------------------------------------------------------------------------
Sorted by: 





npl_grantpubln_personid
-----------------------
Dataset documentation: npl_grantpubln_personid.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/query_sources/

Contains data                                 
  obs:     2,907,265                          6 Jun 2018 08:10
 vars:             6                          
 size:    66,867,095                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
appln_id        long    %12.0g                
pat_publn_id    long    %12.0g                
applt_seq_nr    byte    %8.0g                 
person_id       long    %12.0g                
han_id          long    %12.0g                
publn_date      int     %td                   
-------------------------------------------------------------------------------
Sorted by: 





npl_firstpubln_personid
-----------------------
Dataset documentation: npl_firstpubln_personid.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/query_sources/

Contains data                                 
  obs:     4,584,470                          6 Jun 2018 09:33
 vars:             6                          
 size:   105,442,810                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
appln_id        long    %12.0g                
pat_publn_id    long    %12.0g                
applt_seq_nr    byte    %8.0g                 
person_id       long    %12.0g                
han_id          long    %12.0g                
publn_date      int     %td                   
-------------------------------------------------------------------------------
Sorted by: 





scowos_npl_match_hq_idonly
--------------------------
Dataset documentation: scowos_npl_match_hq_idonly.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl/

Contains data                                 
  obs:    12,509,427                          20 Jan 2018 16:59
 vars:             2                          
 size:   400,301,664                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pat_publn_id_str
                str9    %9s                   
id              str19   %19s                  
-------------------------------------------------------------------------------
Sorted by: 





DBLP_npl_citing_bvdids
----------------------
Dataset documentation: DBLP_npl_citing_bvdids.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:       505,754                          11 Mar 2019 16:57
 vars:             5                          
 size:    82,943,656                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
citing_appln_id long    %12.0g                application id PATSTAT (long)
citing_applt_seq_nr
                byte    %8.0g                 
person_name_component
                str46   %46s                  
han_name_component
                str46   %46s                  
-------------------------------------------------------------------------------
Sorted by: key_resource  





dblp_affiliations
-----------------
Dataset documentation: dblp_affiliations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     5,071,675                          11 Mar 2019 17:04
 vars:            10                          
 size: 2,119,960,150                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
crosref         str37   %37s                  
type            str13   %13s                  
id              str19   %19s                  ID
query           str263  %263s                 
pk_addresses    long    %8.0g                 
addr_number     int     %8.0g                 
sequence_nr     int     %10.0g                
pk_affiliations double  %10.0g                
conf_type       str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: key_resource  





dblp_affiliations_bvdids
------------------------
Dataset documentation: dblp_affiliations_bvdids.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:       417,780                          11 Mar 2019 17:05
 vars:             4                          
 size:    56,818,080                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
id              str19   %19s                  ID
participant_component
                str48   %48s                  
participant_component_seq_nr
                int     %10.0g                (min) sequence_nr
-------------------------------------------------------------------------------
Sorted by: key_resource  id  participant_component  





conf_vol_series_cleaned
-----------------------
Dataset documentation: conf_vol_series_cleaned.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:        27,278                          11 Mar 2019 17:05
 vars:             3                          
 size:     3,218,804                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
crosref         str33   %33s                  crosref
conf_dblp_id    str21   %21s                  conf_dblp_id
id_event        str60   %60s                  
-------------------------------------------------------------------------------
Sorted by: 





df_impute_date_manual
---------------------
Dataset documentation: df_impute_date_manual.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:         1,721                          11 Mar 2019 17:05
 vars:             4                          
 size:       777,892                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
title           str438  %438s                 title
year            int     %10.0g                start_year
start_date_t    float   %td                   
end_date_t      float   %td                   
-------------------------------------------------------------------------------
Sorted by: 





df_geocode_missing
------------------
Dataset documentation: df_geocode_missing.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:           169                          11 Mar 2019 17:05
 vars:             7                          
 size:        11,999                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
city_clean      str26   %26s                  city_clean
country         str14   %14s                  country
country_code    str2    %9s                   country_code
lat             double  %10.0g                lat
lon             double  %10.0g                lon
new_country     str7    %9s                   new_country
new_country_code
                str2    %9s                   new_country_code
-------------------------------------------------------------------------------
Sorted by: 





df_impute_loc_manual
--------------------
Dataset documentation: df_impute_loc_manual.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:         2,819                          11 Mar 2019 17:05
 vars:             4                          
 size:     1,389,767                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
title           str438  %438s                 title
city            str26   %26s                  city
country         str22   %22s                  country
country_code    str3    %9s                   country_code
-------------------------------------------------------------------------------
Sorted by: 





conf_series_cleaned
-------------------
Dataset documentation: conf_series_cleaned.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     1,864,229                          11 Mar 2019 17:06
 vars:             9                          
 size:   426,908,441                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
crosref         str37   %37s                  
year            int     %8.0g                 start_year
city_clean      str31   %31s                  city_clean
lat_city        float   %9.0g                 
lon_city        float   %9.0g                 
country_code    str3    %9s                   country_code
conf_dblp_id    str21   %21s                  conf_dblp_id
id_event        str60   %60s                  
key_resource    str63   %63s                  
-------------------------------------------------------------------------------
Sorted by: 





dblp_citation_links_year
------------------------
Dataset documentation: dblp_citation_links_year.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Within-DBLP citation links
                                                based on Scopus citation links
  obs:    46,847,925                          13 Jul 2018 16:11
 vars:             6                          
 size: 8,057,843,100                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
citing_key_resource
                str63   %63s                  DBLP item which did the citing
citing_items_id str19   %19s                  Scopus ID of the citing item
citing_year     int     %10.0g                DBLP publication year of the
                                                citing item
cited_key_resource
                str63   %63s                  DBLP item which received the
                                                citation
cited_eid       str19   %19s                  Scopus ID of the cited item
cited_year      int     %10.0g                DBLP publication year of the
                                                cited item
-------------------------------------------------------------------------------
Sorted by: 





author_inventor_match_scowos
----------------------------
Dataset documentation: author_inventor_match_scowos.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/author_inventor/

Contains data                                 Author Inventor Overlap for WoS
                                                & Scopus
  obs:     2,256,288                          11 Jul 2018 19:00
 vars:            10                          
 size:   243,679,104 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pat_publn_id_str
                long    %12.0g                
id              str19   %19s                  
pk_items        double  %12.0g                
PERSON_ID       long    %12.0g                
pk_persons      double  %12.0g                
person_name     strL    %9s                   
lastname        str34   %34s                  
firstname       strL    %9s                   
person_id_scopus
                double  %10.0g                PERSON_ID variable from Scopus
id_type         str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: id  pat_publn_id_str  PERSON_ID  





conf_company_citation_counts
----------------------------
Dataset documentation: conf_company_citation_counts.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 List of companies that cited
                                                DBLP items (window 5 years)
  obs:    13,986,320                          14 Mar 2019 12:43
 vars:            21                          
 size: 1,972,071,120                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str62   %62s                  
company         str48   %48s                  
scicit_other_total
                int     %9.0g                 (count) first_participant
scicit_other_first
                int     %9.0g                 (sum) first_participant
patcit_other_total
                int     %9.0g                 (count) first_patent
patcit_other_first
                byte    %9.0g                 (sum) first_patent
patcit_total    int     %9.0g                 (count) first
patcit_first    byte    %9.0g                 (sum) first
patcit_is_ovl   byte    %9.0g                 (sum) is_overlap
patcit_is_ovl_first
                byte    %9.0g                 (sum) is_overlap_first
scicit_total    int     %9.0g                 # Company citing paper using
                                                science
scicit_first    byte    %9.0g                 # First author company citing
                                                paper using science
patcit_dist2_total
                int     %9.0g                 # Company patents citing papers
                                                citing the focal paper
patcit_dist2_first
                int     %9.0g                 # Company first author patents
                                                citing papers citing the focal
                                                paper
patcit_dist2_same_total
                byte    %9.0g                 # Company patents citing company
                                                papers citing the focal paper
patcit_dist2_same_firstauth
                byte    %9.0g                 # Company patents citing company
                                                papers citing the focal paper
                                                (first author)
patcit_dist2_same_firstboth
                byte    %9.0g                 # Company patents citing company
                                                papers citing the focal paper
                                                (both first)
patcit_idir_total
                int     %9.0g                 # Company patents citing any
                                                papers citing the focal paper
patcit_idir_first
                byte    %9.0g                 # Company first author patents
                                                citing any papers citing the
                                                focal paper
author          byte    %9.0g                 
author_first    byte    %9.0g                 
-------------------------------------------------------------------------------
Sorted by: 

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





conf_company_abstract_similarity
--------------------------------
Dataset documentation: conf_company_abstract_similarity.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:    23,989,363                          15 Oct 2018 15:50
 vars:            22                          
 size: 4,150,159,799                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
company         str60   %60s                  
key_resource    str59   %59s                  
sim_count_1     int     %8.0g                 Science Abstract Similarity:
                                                count_1
sim_count_2     int     %8.0g                 Science Abstract Similarity:
                                                count_2
sim_count_3     int     %8.0g                 Science Abstract Similarity:
                                                count_3
sim_count_4     int     %8.0g                 Science Abstract Similarity:
                                                count_4
sim_count_5     int     %8.0g                 Science Abstract Similarity:
                                                count_5
sim_max_1       int     %8.0g                 Science Abstract Similarity:
                                                max_1
sim_max_2       int     %8.0g                 Science Abstract Similarity:
                                                max_2
sim_max_3       int     %8.0g                 Science Abstract Similarity:
                                                max_3
sim_max_4       int     %8.0g                 Science Abstract Similarity:
                                                max_4
sim_max_5       int     %8.0g                 Science Abstract Similarity:
                                                max_5
sim_mean_1      float   %9.0g                 Science Abstract Similarity:
                                                mean_1
sim_mean_2      float   %8.0g                 Science Abstract Similarity:
                                                mean_2
sim_mean_3      float   %9.0g                 Science Abstract Similarity:
                                                mean_3
sim_mean_4      float   %9.0g                 Science Abstract Similarity:
                                                mean_4
sim_mean_5      float   %9.0g                 Science Abstract Similarity:
                                                mean_5
sim_min_1       int     %8.0g                 Science Abstract Similarity:
                                                min_1
sim_min_2       int     %8.0g                 Science Abstract Similarity:
                                                min_2
sim_min_3       int     %8.0g                 Science Abstract Similarity:
                                                min_3
sim_min_4       int     %8.0g                 Science Abstract Similarity:
                                                min_4
sim_min_5       int     %8.0g                 Science Abstract Similarity:
                                                min_5
-------------------------------------------------------------------------------
Sorted by: 





assignee_georesults
-------------------
Dataset documentation: assignee_georesults.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:       167,209                          30 Jul 2018 19:06
 vars:             4                          
 size:     4,180,225                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
lat             double  %10.0g                
lon             double  %10.0g                
precision_level byte    %18.0g     geo_precision_level
                                              
PERSON_ID       long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





company_patents_applicant_locations
-----------------------------------
Dataset documentation: company_patents_applicant_locations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 List of all patents that
                                                npl-citing companies applied
                                                for, by HAN_ID.
  obs:       333,124                          3 Jul 2018 15:09
 vars:             6                          
 size:    48,969,228                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
person_name_component
                str61   %61s                  
han_name_component
                str61   %61s                  
priority_year   float   %9.0g                 
lat             double  %10.0g                
lon             double  %10.0g                
precision_level byte    %18.0g     geo_precision_level
                                              
-------------------------------------------------------------------------------
Sorted by: 

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





PATSTAT_basic_042017
--------------------
Containing folder: E:/PATSTAT/2017-04/DTA

NOT FOUND


company_inventor_addresses
--------------------------
Dataset documentation: company_inventor_addresses.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/Geocoding/

Contains data                                 
  obs:    12,710,378                          8 Jun 2018 11:41
 vars:             4                          
 size: 3,228,436,012                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
earliest_pat_publn_id
                long    %12.0g                
PERSON_ID       long    %12.0g                
PERSON_ADDRESS  str240  %240s                 
PERSON_CTRY_CODE
                str2    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





inventor_georesults
-------------------
Dataset documentation: inventor_georesults.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:     8,243,281                          30 Jul 2018 19:06
 vars:             4                          
 size:   206,082,025                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
lat             double  %10.0g                
lon             double  %10.0g                
precision_level byte    %18.0g     geo_precision_level
                                              
PERSON_ID       long    %12.0g                
-------------------------------------------------------------------------------
Sorted by: 





company_patents_inventor_locations
----------------------------------
Dataset documentation: company_patents_inventor_locations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 List of all patents that
                                                npl-citing companies applied
                                                for, by HAN_ID.
  obs:    16,399,753                          3 Jul 2018 15:26
 vars:             8                          
 size: 2,509,162,209                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
person_name_component
                str61   %61s                  
han_name_component
                str61   %61s                  
priority_year   int     %9.0g                 
earliest_pat_publn_id
                long    %12.0g                earliest publication number
inventor_person_id
                long    %12.0g                
lat             double  %10.0g                
lon             double  %10.0g                
precision_level byte    %18.0g     geo_precision_level
                                              
-------------------------------------------------------------------------------
Sorted by: 

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





dblp_georesults
---------------
Dataset documentation: dblp_georesults.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:     8,071,332                          30 Jul 2018 18:52
 vars:             6                          
 size:   799,061,868                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
id              str19   %19s                  ID
lat             float   %10.0g                
lon             float   %10.0g                
precision_level byte    %18.0g     geo_precision_level
                                              
weight_location float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: key_resource  





company_science_locations
-------------------------
Dataset documentation: company_science_locations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:       357,086                          3 Jul 2018 15:28
 vars:             7                          
 size:    48,206,610                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
year            int     %10.0g                
participant_component
                str53   %53s                  
lat             float   %10.0g                
lon             float   %10.0g                
precision_level byte    %18.0g     geo_precision_level
                                              
weight_location float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: 





tmp_persons_bio
---------------
Dataset documentation: tmp_persons_bio.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     9,789,793                          23 Jul 2019 18:55
 vars:             5                          
 size: 1,272,673,090                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
personname      str57   %57s                  
order           int     %8.0g                 
n_persons       int     %8.0g                 
year            int     %10.0g                
-------------------------------------------------------------------------------
Sorted by: 





author_previous_participation
-----------------------------
Dataset documentation: author_previous_participation.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Number of papers in same
                                                conference series in previous
                                                years
  obs:     1,805,955                          24 Jul 2019 19:42
 vars:            33                          
 size:   180,595,500                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str62   %62s                  
prevauth_any0   byte    %9.0g                 Overlapping author (# papers, 0
                                                years ago)
prevauth_any1   byte    %9.0g                 Overlapping author (# papers, 1
                                                years ago)
prevauth_any2   byte    %9.0g                 Overlapping author (# papers, 2
                                                years ago)
prevauth_any3   byte    %9.0g                 Overlapping author (# papers, 3
                                                years ago)
prevauth_any4   byte    %9.0g                 Overlapping author (# papers, 4
                                                years ago)
prevauth_any5   byte    %9.0g                 Overlapping author (# papers, 5
                                                years ago)
prevauth_any_w3 int     %9.0g                 Overlapping author (# papers, 3
                                                years ago)
prevauth_any_w5 int     %9.0g                 Overlapping author (# papers, 5
                                                years ago)
prevauth_both_first0
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers, 0 years ago)
prevauth_both_first1
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers, 1 years ago)
prevauth_both_first2
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers, 2 years ago)
prevauth_both_first3
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers, 3 years ago)
prevauth_both_first4
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers, 4 years ago)
prevauth_both_first5
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers, 5 years ago)
prevauth_both_first_w3
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers within 3 years)
prevauth_both_first_w5
                byte    %9.0g                 Overlapping author first author
                                                current+previous paper (#
                                                papers within 5 years)
prevauth_then_first0
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers, 0 years ago)
prevauth_then_first1
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers, 1 years ago)
prevauth_then_first2
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers, 2 years ago)
prevauth_then_first3
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers, 3 years ago)
prevauth_then_first4
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers, 4 years ago)
prevauth_then_first5
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers, 5 years ago)
prevauth_then_first_w3
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers within 3 years)
prevauth_then_first_w5
                byte    %9.0g                 Overlapping author was first
                                                author on previous paper (#
                                                papers within 5 years)
prevauth_now_first0
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers, 0 years ago)
prevauth_now_first1
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers, 1 years ago)
prevauth_now_first2
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers, 2 years ago)
prevauth_now_first3
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers, 3 years ago)
prevauth_now_first4
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers, 4 years ago)
prevauth_now_first5
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers, 5 years ago)
prevauth_now_first_w3
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers within 3
                                                years)
prevauth_now_first_w5
                byte    %9.0g                 Overlapping author is now first
                                                author (# papers within 5
                                                years)
-------------------------------------------------------------------------------
Sorted by: key_resource  

_dta:
  1.  "Variables on being first author also contained"
  2.  "Variable on same-year excludes the paper itself; it is the number of
      other papers on the same conference series"
  3.  "Creation date 24 Jul 2019 19:38 "
  4.  "Creation file build_previous_participation.do"





dblp_citation_links
-------------------
Dataset documentation: dblp_citation_links.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:    32,716,823                          10 Jul 2018 09:30
 vars:             5                          
 size: 1,963,009,380                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_citingitems  long    %10.0g                
fk_items        double  %10.0g                
cited_by_eid    str18   %18s                  
citing_items_id str18   %18s                  
citing_items_fk_items
                double  %10.0g                
-------------------------------------------------------------------------------
Sorted by: 





dblp_citation_links_wos
-----------------------
Dataset documentation: dblp_citation_links_wos.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:    30,711,919                          10 Jul 2018 11:24
 vars:             2                          
 size: 1,289,900,598                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
cited_by_eid    str19   %19s                  
citing_items_id str19   %19s                  
-------------------------------------------------------------------------------
Sorted by: 





conferences_infosci_affiliations
--------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences

NOT FOUND


npl_applicant_names
-------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl

NOT FOUND


pat_han_names
-------------
Dataset documentation: pat_han_names.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/query_sources/

Contains data                                 TLS906 - Names & Addresses by
                                                Person_ID - PATSTAT042017
  obs:     1,404,716                          27 Feb 2018 17:49
 vars:             6                          
 size: 1,060,560,580                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
person_id       long    %12.0g                
person_name     str354  %354s                 
person_ctry_code
                str2    %9s                   
psn_sector      str33   %33s                  
han_id          long    %12.0g                
han_name        str354  %354s                 
-------------------------------------------------------------------------------
Sorted by: person_id  





bing_match_string_frequency
---------------------------
Dataset documentation: bing_match_string_frequency.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     1,906,054                          16 May 2018 14:29
 vars:             3                          
 size:    47,651,350 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
query           strL    %9s                   
type            str5    %9s                   
count           double  %9.0g                 (sum) count
-------------------------------------------------------------------------------
Sorted by: count  





scopus_dblp_classifications
---------------------------
Dataset documentation: scopus_dblp_classifications.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     5,569,761                          1 Mar 2018 09:24
 vars:             2                          
 size:   133,674,264                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id              str18   %18s                  
classification  int     %10.0g                
-------------------------------------------------------------------------------
Sorted by: 





scopus_dblp_classifications_weighted
------------------------------------
Dataset documentation: scopus_dblp_classifications_weighted.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 ASJC classifications for DBLP
                                                items as determined by Scopus
                                                items only
  obs:     5,564,807                          11 May 2018 14:30
 vars:             3                          
 size:   428,490,139                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
asjc            int     %10.0g                All Journal Science
                                                Classification
weight_asjc     double  %9.0g                 Sum of: 1 / (N classifications) /
                                                (N linked scopus items)
-------------------------------------------------------------------------------
Sorted by: key_resource  asjc  





wos_dblp_classifications_weighted
---------------------------------
Dataset documentation: wos_dblp_classifications_weighted.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     4,300,330                          1 Mar 2018 15:46
 vars:             3                          
 size:   331,125,410                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
wossoc          str2    %9s                   
weight_wossoc   double  %9.0g                 (sum) weight_wossoc
-------------------------------------------------------------------------------
Sorted by: wossoc  key_resource  





concordance_dblp_wos_sco_classifications
----------------------------------------
Dataset documentation: concordance_dblp_wos_sco_classifications.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 DBLP-based Scopus/WoS science
                                                area concordance table
  obs:         4,542                          1 Mar 2018 15:49
 vars:             4                          
 size:        72,672                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
asjc            int     %10.0g                Scopus ASJC classification
wossoc          str2    %9s                   WoS science classification
factor_asjc     float   %9.0g                 Factor ASJC -> WoS
factor_wossoc   float   %9.0g                 Factor WoS -> ASJC
-------------------------------------------------------------------------------
Sorted by: wossoc  





npl_wos_barebone
----------------
Dataset documentation: npl_wos_barebone.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl/

Contains data                                 NPL Citations Data from DOCDB
                                                after 1st Cleaning Round
  obs:    31,182,674                          2 Mar 2018 19:02
 vars:            34                          
 size: 3,523,642,162                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pat_publn_id_str
                str9    %9s                   
cits_phase      str3    %9s                   docdb cited-phase field
cits_pos_npl    int     %10.0g                docdb nplcit-num field (counter
                                                for nplcits only)
cits_docid      long    %10.0g                docdb docid
publn_auth      str2    %9s                   publication authority PATSTAT
                                                (str2)
publn_nr        str12   %12s                  publication number PATSTAT
                                                (str15)
publn_kind      str2    %9s                   publication kind PATSTAT (str2)
appln_id        long    %12.0g                application id PATSTAT (long)
publn_date      int     %12.0g                
soma_epot_id    long    %12.0g                mpdl unique id
soma_item_ut    str19   %19s                  web of science ut number
soma_pattern    str6    %9s                   mpdl matching quality pattern
soma_class      byte    %8.0g                 mpdl matching quality class (sum
                                                of all digits of soma_pattern)
_merge_MPDL_DOCDB
                byte    %23.0g     _merge     
appln_auth      str2    %9s                   application authority
docdb_family_id long    %12.0g                id for DOCDB family (long)
earliest_filing_date
                int     %d                    earliest filing date
priority_year   int     %9.0g                 priority year
X_cite          byte    %8.0g                 
Y_cite          byte    %8.0g                 
A_cite          byte    %8.0g                 
E_cite          byte    %8.0g                 
oth_cite        byte    %8.0g                 Not X, Y, A, E citation
D_cite          byte    %8.0g                 
T_cite          byte    %8.0g                 
WOEP_link       float   %9.0g                 WO filing linked to EP filing
                                                (equivalent) (Get data in
                                                WOEP_ctng_new)
item_id         long    %12.0g                unique item identifier (primary
                                                key)
item_pt         str1    %9s                   ITEM_PT
item_dt         str2    %9s                   documenttype (DT)
item_dto        str1    %9s                   ITEM_DTO
item_dtn        str2    %9s                   ITEM_DTN
item_py         int     %8.0g                 publication year (PY)
item_june_id    long    %12.0g                journal title identifier, foreign
                                                key to june_id
_merge_WOS      byte    %23.0g     _merge     
-------------------------------------------------------------------------------
Sorted by: 

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





${DTA_OUTPUT}npl_publication_dates
----------------------------------
Containing folder: 

NOT FOUND


appln_granted_applicant_types_raw
---------------------------------
Dataset documentation: appln_granted_applicant_types_raw.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl_cit_flows/

Contains data                                 
  obs:     9,461,605                          5 Jun 2018 15:52
 vars:             7                          
 size:   596,081,115                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
appln_id        long    %12.0g                
pat_publn_id    long    %12.0g                
applt_seq_nr    int     %8.0g                 
person_id       long    %12.0g                
han_id          long    %12.0g                
psn_sector      str33   %33s                  
publn_date      double  %td                   
-------------------------------------------------------------------------------
Sorted by: 





conf_npl_invt_auth_overlap
--------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon

NOT FOUND


tmp_event_citation_counts
-------------------------
Dataset documentation: tmp_event_citation_counts.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Within-DBLP citation links
                                                based on Scopus citation links
  obs:        22,554                          11 Jun 2019 14:44
 vars:             8                          
 size:     2,435,832                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id_event        str60   %60s                  Unique ID for a conference event
count_items     double  %9.0g                 (sum) count_items
event_count_within_5
                double  %9.0g                 (sum) event_count_within_5
event_count_within_ever
                double  %9.0g                 (sum) event_count_within_ever
event_count_within_scowos
                double  %9.0g                 (sum) event_count_within_scowos
event_avg_within_5
                float   %9.0g                 
event_avg_within_ever
                float   %9.0g                 
event_avg_within_scowos
                float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: id_event  





tmp_bing_res_manual
-------------------
Dataset documentation: tmp_bing_res_manual.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     1,893,765                          10 Mar 2019 21:03
 vars:             4                          
 size:   267,020,865                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
clean_name      str15   %15s                  clean_name
component_name  str69   %69s                  component_name
bvd_id_number   str49   %49s                  bvd_id_number
version         float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: 





bvd_id_components
-----------------
Dataset documentation: bvd_id_components.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:        15,320                          11 Mar 2019 15:23
 vars:             8                          
 size:     2,405,240                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
clean_name      str15   %15s                  clean_name
component_name  str69   %69s                  component_name
bvd_id_number   str49   %49s                  bvd_id_number
is_scoreboard   float   %9.0g                 
is_grid         float   %9.0g                 
drop_bvd_id     float   %9.0g                 
scoreboard_component
                float   %9.0g                 
grid_component  float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: component_name  





Scoreboard
----------
Dataset documentation: Scoreboard.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/orig/Scoreboard/

Contains data                                 
  obs:        37,760                          10 Mar 2019 20:23
 vars:            11                          
 size:    11,290,240                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
Rank            int     %10.0g                
Company         str87   %87s                  
Company_clean   str56   %56s                  
Country         str35   %35s                  
RnD_Investment  double  %10.0g                
Net_Sales       double  %10.0g                
Employees       double  %10.0g                
Year            float   %9.0g                 
Scoreboard_type str6    %9s                   
Sector          str43   %43s                  
UnifiedSector   str38   %38s                  Unified Sector
-------------------------------------------------------------------------------
Sorted by: 





bvd_id_components_countries
---------------------------
Dataset documentation: bvd_id_components_countries.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:         4,828                          11 Mar 2019 15:23
 vars:             8                          
 size:       502,112                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
component_name  str69   %69s                  component_name
scoreboard_component
                float   %9.0g                 
final_country   str7    %9s                   
has_DE          float   %9.0g                 
has_US          float   %9.0g                 
has_JP          float   %9.0g                 
has_KR          float   %9.0g                 
has_CN          float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: component_name  





tmp_bing_manual_additions, generate(appended)
---------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon

NOT FOUND


cluster_all_final_pre
---------------------
Dataset documentation: cluster_all_final_pre.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/final/

Contains data                                 
  obs:       743,748                          11 Mar 2019 15:24
 vars:             2                          
 size:   213,455,676                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
query           str235  %235s                 
company_name    str48   %48s                  
-------------------------------------------------------------------------------
Sorted by: query  





cluster_all_final_pre, gen(appended)
------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/bing/final

NOT FOUND


wos_publication_dates
---------------------
Dataset documentation: wos_publication_dates.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl/

Contains data                                 
  obs:    54,697,131                          16 Aug 2018 14:26
 vars:             5                          
 size: 2,898,947,943                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
item_ut         str19   %19s                  
item_id         double  %10.0g                
date_type       str6    %6s                   
date_1          double  %td                   
date_2          double  %td                   
-------------------------------------------------------------------------------
Sorted by: 





wos_backward_diff_agg
---------------------
Dataset documentation: wos_backward_diff_agg.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl/

Contains data                                 
  obs:     4,244,968                          16 Aug 2018 18:09
 vars:             6                          
 size:   203,758,464                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
itre_item_id_from
                double  %10.0g                
mean            double  %10.0g                
count           long    %12.0g                
max             double  %10.0g                
min             double  %10.0g                
p50             double  %10.0g                
-------------------------------------------------------------------------------
Sorted by: 







Containing folder: 

NOT FOUND


wos_citation_lags
-----------------
Dataset documentation: wos_citation_lags.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/npl/

Contains data                                 NPL Citations Data from DOCDB
                                                after 1st Cleaning Round
  obs:     1,055,385                          17 Aug 2018 14:34
 vars:             5                          
 size:    23,218,470                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
docdb_family_id long    %12.0g                (first) docdb_family_id
mean_diff       float   %9.0g                 (mean)
                                                diff_date_mid_appln_filing_date
p90_diff        float   %9.0g                 (p 90)
                                                diff_date_mid_appln_filing_date
count_SNPL      int     %9.0g                 (count)
                                                diff_date_mid_appln_filing_date
ratio_mean      float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: docdb_family_id  

_dta:
  1.  closing state Xb5804563c43f462544a474abacbdd93d00041fb5





conf_series_similarity
----------------------
Dataset documentation: conf_series_similarity.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Within-DBLP citation links
                                                based on Scopus citation links
  obs:       403,903                          14 Aug 2018 10:31
 vars:             6                          
 size:    23,426,374                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
citing_conf_dblp_id
                str17   %17s                  Citing conference series
cited_conf_dblp_id
                str17   %17s                  Cited conference series
p_weight        double  %9.0g                 P(citing conference cites cited
                                                conference)
e_weight        double  %9.0g                 E(#papers in cited conference
                                                that citing conference cites)
citing_conf_size
                int     %9.0g                 # Papers in citing conference
                                                series
cited_conf_size int     %9.0g                 # Papers in cited conference
                                                series
-------------------------------------------------------------------------------
Sorted by: citing_conf_dblp_id  cited_conf_dblp_id  





conf_series_similarity_twoway
-----------------------------
Dataset documentation: conf_series_similarity_twoway.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 Within-DBLP citation links
                                                based on Scopus citation links
  obs:       158,014                          14 Aug 2018 10:43
 vars:             3                          
 size:     6,636,588                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
conf_dblp_id_0  str17   %17s                  Citing conference series
conf_dblp_id_1  str17   %17s                  Cited conference series
p_weight        float   %9.0g                 P(conf0 cites conf1) * P(conf1
                                                cites conf0)
-------------------------------------------------------------------------------
Sorted by: conf_dblp_id_0  conf_dblp_id_1  





coauthorships
-------------
Dataset documentation: coauthorships.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:     2,133,699                          7 Dec 2018 15:42
 vars:             4                          
 size:   305,118,957                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
key_resource    str63   %63s                  
dblp_type       str13   %13s                  
sequence_nr     int     %10.0g                
company_name    str61   %61s                  
-------------------------------------------------------------------------------
Sorted by: key_resource  sequence_nr  





matched_dataset${NAME_SUFFIX}
-----------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/matching

NOT FOUND


components_part_sponsor
-----------------------
Dataset documentation: components_part_sponsor.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/matching/

Contains data                                 
  obs:        78,790                          25 Jul 2019 22:50
 vars:             4                          
 size:     8,351,740                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id_event        str52   %52s                  Unique ID for a conference event
company         str48   %48s                  
is_participant  byte    %9.0g                 (max) is_participant
is_sponsor      byte    %9.0g                 (max) is_sponsor
-------------------------------------------------------------------------------
Sorted by: id_event  company  





conferences_combined_full
-------------------------
Dataset documentation: conferences_combined_full.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/

Contains data                                 
  obs:    15,842,542                          14 Jan 2018 17:59
 vars:            70                          
 size: 8,158,909,130 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %12.0g                
title           strL    %9s                   
conf_type       str3    %9s                   
event_start_year
                int     %10.0g                conf_start YEAR
event_start_month
                byte    %10.0g                conf_start MONTH
event_end_year  int     %10.0g                conf_end YEAR
event_end_month byte    %10.0g                conf_end MONTH
proceed_year    int     %10.0g                
proceed_month   byte    %10.0g                
proceed_day     byte    %10.0g                
proceed_year_first
                int     %10.0g                
proceed_year_last
                int     %10.0g                
event_start_day byte    %10.0g                conf_start DAY
event_end_day   byte    %10.0g                conf_end DAY
postalcode      strL    %9s                   
address_part    strL    %9s                   
city            strL    %9s                   
venue           strL    %9s                   
host            strL    %9s                   
weightagr_agro  double  %10.0g                (sum) weightagr_agro
weightagr_animal
                double  %10.0g                (sum) weightagr_animal
weightagr_other double  %10.0g                (sum) weightagr_other
weightagr_veter double  %10.0g                (sum) weightagr_veter
weighteng_biotech
                double  %10.0g                (sum) weighteng_biotech
weighteng_chem  double  %10.0g                (sum) weighteng_chem
weighteng_civil double  %10.0g                (sum) weighteng_civil
weighteng_electr
                double  %10.0g                (sum) weighteng_electr
weighteng_environ
                double  %10.0g                (sum) weighteng_environ
weighteng_indbiotech
                double  %10.0g                (sum) weighteng_indbiotech
weighteng_material
                double  %10.0g                (sum) weighteng_material
weighteng_mechan
                double  %10.0g                (sum) weighteng_mechan
weighteng_medical
                double  %10.0g                (sum) weighteng_medical
weighteng_other double  %10.0g                (sum) weighteng_other
weighthum_arts  double  %10.0g                (sum) weighthum_arts
weighthum_history
                double  %10.0g                (sum) weighthum_history
weighthum_language
                double  %10.0g                (sum) weighthum_language
weighthum_other double  %10.0g                (sum) weighthum_other
weighthum_philos
                double  %10.0g                (sum) weighthum_philos
weightmed_basic double  %10.0g                (sum) weightmed_basic
weightmed_clin  double  %10.0g                (sum) weightmed_clin
weightmed_health
                double  %10.0g                (sum) weightmed_health
weightnnn       double  %10.0g                (sum) weightnnn
weightsci_biol  double  %10.0g                (sum) weightsci_biol
weightsci_chem  double  %10.0g                (sum) weightsci_chem
weightsci_environ
                double  %10.0g                (sum) weightsci_environ
weightsci_infosci
                double  %10.0g                (sum) weightsci_infosci
weightsci_mathem
                double  %10.0g                (sum) weightsci_mathem
weightsci_other double  %10.0g                (sum) weightsci_other
weightsci_physics
                double  %10.0g                (sum) weightsci_physics
weightsoc_commun
                double  %10.0g                (sum) weightsoc_commun
weightsoc_econ  double  %10.0g                (sum) weightsoc_econ
weightsoc_educ  double  %10.0g                (sum) weightsoc_educ
weightsoc_geogr double  %10.0g                (sum) weightsoc_geogr
weightsoc_law   double  %10.0g                (sum) weightsoc_law
weightsoc_other double  %10.0g                (sum) weightsoc_other
weightsoc_politics
                double  %10.0g                (sum) weightsoc_politics
weightsoc_psychol
                double  %10.0g                (sum) weightsoc_psychol
weightsoc_sociol
                double  %10.0g                (sum) weightsoc_sociol
weightAgriculture
                double  %10.0g                (sum) weightAgriculture
weightEngineering
                double  %10.0g                (sum) weightEngineering
weightHumanities
                double  %10.0g                (sum) weightHumanities
weightMedicine  double  %10.0g                (sum) weightMedicine
weightNot_known double  %10.0g                (sum) weightNot_known
weightScience   double  %10.0g                (sum) weightScience
weightSocial_Science
                double  %10.0g                (sum) weightSocial_Science
weightUnknown   double  %10.0g                (sum) weightUnknown
weightBAUSTELLE double  %10.0g                (sum) weightBAUSTELLE
weighteng_materials
                double  %10.0g                (sum) weighteng_materials
state           str24   %24s                  new_state
country         str20   %20s                  new_country
-------------------------------------------------------------------------------
Sorted by: 





sco_conf_to_pk_affiliations
---------------------------
Dataset documentation: sco_conf_to_pk_affiliations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/sco_prep/

Contains data                                 
  obs:    26,413,941                          4 Jul 2018 09:35
 vars:             5                          
 size: 1,267,869,168                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
pk_conferences  double  %10.0g                
id              str18   %18s                  
fk_items        double  %10.0g                
fk_affiliations double  %10.0g                
sequence_nr     int     %10.0g                
-------------------------------------------------------------------------------
Sorted by: 





core_fields
-----------
Dataset documentation: core_fields.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/conf_spon/

Contains data                                 
  obs:            36                          3 Nov 2018 15:25
 vars:             2                          
 size:         1,908                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
core_field      int     %8.0g                 Field_code
core_field_name str47   %47s                  Field
-------------------------------------------------------------------------------
Sorted by: 





company_applicant_addresses
---------------------------
Dataset documentation: company_applicant_addresses.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/Geocoding/

Contains data                                 
  obs:       116,464                          8 Jun 2018 14:13
 vars:             3                          
 size:    28,184,288                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
PERSON_ID       long    %12.0g                
PERSON_ADDRESS  str232  %232s                 
PERSON_CTRY_CODE
                str2    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





patstat_address_personid_list
-----------------------------
Dataset documentation: patstat_address_personid_list.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/PERSONEN/Felix Poege/Geocoding_results/

Contains data                                 
  obs:     4,820,404                          17 Apr 2018 16:35
 vars:             2                          
 size:    57,844,848                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
PERSON_ID       long    %12.0g                
ADDRESS_ID      float   %9.0g                 
-------------------------------------------------------------------------------
Sorted by: 





company_applicant_to_geocode
----------------------------
Dataset documentation: company_applicant_to_geocode.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/Geocoding/

Contains data                                 
  obs:        39,434                          8 Jun 2018 14:16
 vars:             2                          
 size:     9,385,292                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
PERSON_ADDRESS  str232  %232s                 
PERSON_CTRY_CODE
                str2    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





PATSTAT_basic_102017
--------------------
Containing folder: E:/PATSTAT/2017-10/DTA

NOT FOUND


company_inventor_to_geocode
---------------------------
Dataset documentation: company_inventor_to_geocode.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/Output/Data/Geocoding/

Contains data                                 
  obs:       623,044                          8 Jun 2018 14:07
 vars:             2                          
 size:   153,268,824                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
PERSON_ADDRESS  str240  %240s                 
PERSON_CTRY_CODE
                str2    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





`filename'`i'
-------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/orig/Geocoding

NOT FOUND


scowos_results
--------------
Dataset documentation: scowos_results.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:     3,338,086                          27 Jul 2018 23:39
 vars:             7                          
 size: 2,500,226,414                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
address         str399  %399s                 
ctry            str3    %9s                   
lat             float   %10.0g                
lon             float   %10.0g                
match_level     str167  %167s                 
match_code      str167  %167s                 
precision_level byte    %18.0g     geo_precision_level
                                              
-------------------------------------------------------------------------------
Sorted by: 





`filename'`i'
-------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/orig/Geocoding/Patstat/wave1

NOT FOUND


`filename'`i'
-------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/NPL/orig/Geocoding/Patstat/wave2

NOT FOUND


patent_results_raw
------------------
Dataset documentation: patent_results_raw.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:     1,533,201                          3 Jul 2018 14:35
 vars:             7                          
 size:   843,260,550 + strLs
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
ctry            str2    %9s                   
address         strL    %9s                   
lat             float   %10.0g                
lon             float   %10.0g                
label           str200  %200s                 
match_level     str164  %164s                 
match_code      str164  %164s                 
-------------------------------------------------------------------------------
Sorted by: 





scopus_dblp_affiliation_locations
---------------------------------
Dataset documentation: scopus_dblp_affiliation_locations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/dblp_match/

Contains data                                 
  obs:    11,365,312                          25 Jul 2018 04:47
 vars:             8                          
 size:25,640,143,872                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id              str18   %18s                  
sequence_nr     int     %10.0g                
pk_affiliations double  %10.0g                
country_code    str3    %9s                   
country         str1    %9s                   
text            str2016 %2016s                
address_part    str127  %127s                 
city_group      str77   %77s                  
-------------------------------------------------------------------------------
Sorted by: 





wos_dblp_affiliation_locations
------------------------------
Dataset documentation: wos_dblp_affiliation_locations.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/conferences/dblp_match/

Contains data                                 
  obs:     5,553,442                          25 Jul 2018 15:53
 vars:             7                          
 size: 1,144,009,052                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
id              str19   %19s                  
pk_addresses    long    %10.0g                
addr_number     byte    %10.0g                
city            str27   %27s                  
street          str121  %121s                 
country         str15   %15s                  
state           str15   %15s                  
-------------------------------------------------------------------------------
Sorted by: 





country_country_translation
---------------------------
Dataset documentation: country_country_translation.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:         1,184                          8 Jan 2019 16:29
 vars:             2                          
 size:        75,776                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
old_country     str45   %45s                  old_country
new_country     str15   %15s                  new_country
-------------------------------------------------------------------------------
Sorted by: 





country_state_translation
-------------------------
Dataset documentation: country_state_translation.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:         1,976                          8 Jan 2019 16:29
 vars:             4                          
 size:       221,312                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
old_state       str24   %24s                  old_state
old_country     str45   %45s                  old_country
new_state       str24   %24s                  new_state
new_country     str15   %15s                  new_country
-------------------------------------------------------------------------------
Sorted by: 





patent_address_lat_lon_list
---------------------------
Dataset documentation: patent_address_lat_lon_list.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/PERSONEN/Felix Poege/Geocoding_results/

Contains data                                 
  obs:     4,280,691                          11 Apr 2018 09:30
 vars:             9                          
 size: 3,107,781,666                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
ADDRESS_ID      float   %9.0g                 
address_n       byte    %10.0g                
address         str356  %356s                 
ctry            str2    %9s                   
lat             double  %9.0g                 
lon             double  %9.0g                 
match_level     str171  %171s                 
match_code      str171  %171s                 
precision_level byte    %18.0g     geo_precision_level
                                              
-------------------------------------------------------------------------------
Sorted by: ADDRESS_ID  address  ctry  





country_verification
--------------------
Dataset documentation: country_verification.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:           168                          23 Aug 2018 16:52
 vars:             2                          
 size:         5,208                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
iso3            str3    %9s                   iso3
country_long    str24   %24s                  long
-------------------------------------------------------------------------------
Sorted by: 





wos_results
-----------
Dataset documentation: wos_results.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:     1,326,106                          20 Mar 2018 11:38
 vars:             7                          
 size:   612,660,972                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
address         str136  %136s                 
ctry            str1    %9s                   
lat             float   %10.0g                
lon             float   %10.0g                
match_level     str156  %156s                 
match_code      str156  %156s                 
precision_level byte    %18.0g     geo_precision_level
                                              
-------------------------------------------------------------------------------
Sorted by: 





scopus_results
--------------
Dataset documentation: scopus_results.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:     1,929,764                          20 Mar 2018 11:33
 vars:             5                          
 size:   800,852,060                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
address         str399  %399s                 
ctry            str3    %9s                   
lat             float   %10.0g                
lon             float   %10.0g                
precision_level byte    %18.0g     geo_precision_level
                                              
-------------------------------------------------------------------------------
Sorted by: 





scowos_to_geocode
-----------------
Dataset documentation: scowos_to_geocode.dta
-------------------------------------------------------------------------------
Containing folder: X:/Prof. Harhoff/Harhoff_INTERN/FORSCHUNG/Bibliometrics/WoS/DATA/geocoding/

Contains data                                 
  obs:        76,392                          25 Jul 2018 20:17
 vars:             2                          
 size:   154,541,016                          
-------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
-------------------------------------------------------------------------------
address         str2016 %2016s                
ctry            str3    %9s                   
-------------------------------------------------------------------------------
Sorted by: 





${IN_DATA}
----------
Containing folder: 

NOT FOUND

