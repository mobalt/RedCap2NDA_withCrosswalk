import pandas as pd
import numpy as np
import yaml

with open('CONST.yml', 'r') as fd:
    CONST = yaml.load(fd.read(), Loader=yaml.SafeLoader)

fn = {}

def __increment_0_to_2(studydata, column, context):
    """Please increment codes of 0, 1, and 2, but leave code 4 as it is."""
    return column.replace({0:1,1:2,2:3}).astype('Int64')

fn["asr1"]=__increment_0_to_2
fn["asr2"]=__increment_0_to_2
fn["asr3"]=__increment_0_to_2
fn["asr4"]=__increment_0_to_2
fn["asr5"]=__increment_0_to_2
fn["asr6"]=__increment_0_to_2
fn["asr7"]=__increment_0_to_2
fn["asr8"]=__increment_0_to_2
fn["asr9"]=__increment_0_to_2
fn["asr10"]=__increment_0_to_2
fn["asr11"]=__increment_0_to_2
fn["asr12"]=__increment_0_to_2
fn["asr13"]=__increment_0_to_2
fn["asr14"]=__increment_0_to_2
fn["asr15"]=__increment_0_to_2
fn["asr16"]=__increment_0_to_2
fn["asr17"]=__increment_0_to_2
fn["asr18"]=__increment_0_to_2
fn["asr19"]=__increment_0_to_2
fn["asr20"]=__increment_0_to_2
fn["asr21"]=__increment_0_to_2
fn["asr22"]=__increment_0_to_2
fn["asr23"]=__increment_0_to_2
fn["asr24"]=__increment_0_to_2
fn["asr25"]=__increment_0_to_2
fn["asr26"]=__increment_0_to_2
fn["asr27"]=__increment_0_to_2
fn["asr28"]=__increment_0_to_2
fn["asr29"]=__increment_0_to_2
fn["asr30"]=__increment_0_to_2
fn["asr31"]=__increment_0_to_2
fn["asr32"]=__increment_0_to_2
fn["asr33"]=__increment_0_to_2
fn["asr34"]=__increment_0_to_2
fn["asr35"]=__increment_0_to_2
fn["asr36"]=__increment_0_to_2
fn["asr37"]=__increment_0_to_2
fn["asr38"]=__increment_0_to_2
fn["asr39"]=__increment_0_to_2
fn["asr40"]=__increment_0_to_2
fn["asr41"]=__increment_0_to_2
fn["asr42"]=__increment_0_to_2
fn["asr43"]=__increment_0_to_2
fn["asr44"]=__increment_0_to_2
fn["asr45"]=__increment_0_to_2
fn["asr46"]=__increment_0_to_2
fn["asr47"]=__increment_0_to_2
fn["asr48"]=__increment_0_to_2
fn["asr49"]=__increment_0_to_2
fn["asr50"]=__increment_0_to_2
fn["asr51"]=__increment_0_to_2
fn["asr52"]=__increment_0_to_2
fn["asr53"]=__increment_0_to_2
fn["asr54"]=__increment_0_to_2
fn["asr55"]=__increment_0_to_2
fn["asr56a"]=__increment_0_to_2
fn["asr56b"]=__increment_0_to_2
fn["asr56c"]=__increment_0_to_2
fn["asr56d"]=__increment_0_to_2
fn["asr56e"]=__increment_0_to_2
fn["asr56f"]=__increment_0_to_2
fn["asr56g"]=__increment_0_to_2
fn["asr56h"]=__increment_0_to_2
fn["asr56i"]=__increment_0_to_2
fn["asr57"]=__increment_0_to_2
fn["asr58"]=__increment_0_to_2
fn["asr59"]=__increment_0_to_2
fn["asr60"]=__increment_0_to_2
fn["asr61"]=__increment_0_to_2
fn["asr62"]=__increment_0_to_2
fn["asr63"]=__increment_0_to_2
fn["asr64"]=__increment_0_to_2
fn["asr65"]=__increment_0_to_2
fn["asr66"]=__increment_0_to_2
fn["asr67"]=__increment_0_to_2
fn["asr68"]=__increment_0_to_2
fn["asr69"]=__increment_0_to_2
fn["asr70"]=__increment_0_to_2
fn["asr71"]=__increment_0_to_2
fn["asr72"]=__increment_0_to_2
fn["asr73"]=__increment_0_to_2
fn["asr74"]=__increment_0_to_2
fn["asr75"]=__increment_0_to_2
fn["asr76"]=__increment_0_to_2
fn["asr77"]=__increment_0_to_2
fn["asr78"]=__increment_0_to_2
fn["asr79"]=__increment_0_to_2
fn["asr80"]=__increment_0_to_2
fn["asr81"]=__increment_0_to_2
fn["asr82"]=__increment_0_to_2
fn["asr83"]=__increment_0_to_2
fn["asr84"]=__increment_0_to_2
fn["asr85"]=__increment_0_to_2
fn["asr86"]=__increment_0_to_2
fn["asr87"]=__increment_0_to_2
fn["asr88"]=__increment_0_to_2
fn["asr89"]=__increment_0_to_2
fn["asr90"]=__increment_0_to_2
fn["asr91"]=__increment_0_to_2
fn["asr92"]=__increment_0_to_2
fn["asr93"]=__increment_0_to_2
fn["asr94"]=__increment_0_to_2
fn["asr95"]=__increment_0_to_2
fn["asr96"]=__increment_0_to_2
fn["asr97"]=__increment_0_to_2
fn["asr98"]=__increment_0_to_2
fn["asr99"]=__increment_0_to_2
fn["asr100"]=__increment_0_to_2
fn["asr101"]=__increment_0_to_2
fn["asr102"]=__increment_0_to_2
fn["asr103"]=__increment_0_to_2
fn["asr104"]=__increment_0_to_2
fn["asr105"]=__increment_0_to_2
fn["asr106"]=__increment_0_to_2
fn["asr107"]=__increment_0_to_2
fn["asr108"]=__increment_0_to_2
fn["asr109"]=__increment_0_to_2
fn["asr110"]=__increment_0_to_2
fn["asr111"]=__increment_0_to_2
fn["asr112"]=__increment_0_to_2
fn["asr113"]=__increment_0_to_2
fn["asr114"]=__increment_0_to_2
fn["asr115"]=__increment_0_to_2
fn["asr116"]=__increment_0_to_2
fn["asr117"]=__increment_0_to_2
fn["asr118"]=__increment_0_to_2
fn["asr119"]=__increment_0_to_2
fn["asr120"]=__increment_0_to_2
fn["asr121"]=__increment_0_to_2
fn["asr122"]=__increment_0_to_2
fn["asr123"]=__increment_0_to_2

def height(studydata, column, context):
    """Please convert heights to inches."""
    h = column.str.extract('^(?P<feet>[0-9.]+)(?:[^0-9.]+(?P<inches>[0-9.]+))?')
    h = 12 * h.feet.astype(float) + h.inches.astype(float)
    return h.fillna(0)
fn["height"]=height

def bpressure(studydata, column, context):
    return column.str.replace('_', '')
fn['bpressure'] = bpressure


def colorvsn1(studydata, column, context):
    """Please convert numeric codes of 0 and 99 to the text strings they represent."""
    return column.mask(column == 0, 'No').mask(column > 90, "Don't Know")
fn["colorvsn1"]=colorvsn1

def sub_adopt_1(studydata, column, context):
    """Age at adoption is a free-text field. Please concatenate responses from 'sub_adopt_1' and 'sub_adopt_1unit' in the 'sub_adopt_1' column."""

    return column.astype('Int64').astype(str) + studydata.sub_adopt_1unit.replace({1: ' Months', 2: ' Years'})
fn["sub_adopt_1"]=sub_adopt_1

def __convert_country_code_to_text(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['country_codes'])


fn["sub_country"]=__convert_country_code_to_text

def sub_gender(studydata, column, context):
    """Gender identity is a free-text field. Please concatenate responses from 'sub_gender' and 'sub_gender_different' in the 'sub_gender' column."""
    return column.astype(str).replace(CONST['gender']) + studydata.sub_gender_different
fn["sub_gender"]=sub_gender

def sub_marriage(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['marriage_status'])
fn["sub_marriage"]=sub_marriage

def sub_grade(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['education'])
fn["sub_grade"]=sub_grade

def sub_job(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    """Because 'sub_job' is a free-text field, please concatenate subjects' specified answers with 'sub_job' answers."""
    return column.replace(CONST['working_status']) + studydata.sub_job8_1
fn["sub_job"]=sub_job

def sub_job8_1(studydata, column, context):
    pass
fn["sub_job8_1"]=sub_job8_1

def sub_income_num(studydata, column, context):
    """Please us 98 as the missing code, rather than 999999."""
    return column.replace({99: 98, 999999: 98})
fn["sub_income_num"]=sub_income_num

fn["sub_bio_f_country"]=__convert_country_code_to_text
fn["sub_bio_m_county"]=__convert_country_code_to_text

def sub_mgrade(studydata, column, context):
    """Please recode 13 as 14 (for "High school graduate"), 14 as 13 (for "GED or equivalent"), 15 as 16 (for "Some college, no degree"), 16 as 17 (for "Associate degree: occupational/technical/vocational program"), 17 as 18 (for "Associate degree: academic program"), 18 as 20 (for "Bachelor degree (e.g., BA, AB, BS, BBA)"), 19 as 22 (for "Master's degree (e.g., MA, MS, MEng, MEd, MBA)"), 20 as 23 (for "Professional school degree (e.g., MD, DDS, DVM, JD)"), and 21 as 24 (for "Doctoral degree (e.g., PhD, EdD)")."""
    return column.replace({13:14,14:13,15:16,16:17,17:18,18:20,19:22,20:23,21:24})
fn["sub_mgrade"]=sub_mgrade
fn["sub_fgrade"]=sub_mgrade # same logic as above

def dummy_var14(studydata, column, context):
    """Please specify a time range of "Past 4 weeks" for all records."""
    studydata['version_form']='Past 4 weeks'
fn["dummy_var14"]=dummy_var14

def mctq_free9(studydata, column, context):
    """Please combine mctq_free9 and mctq_free10 under one column (either name would be fine). Please also convert mctq_free9's numeric codes to the text strings they represent."""
    return column.replace({
        1: 'Familymembers/pet(s)',
        2: 'Hobbies',
        3: 'Other: ',
    }) + studydata.mctq_free10
fn["mctq_free9"]=mctq_free9

def __decrement_1_5_to_0_4(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    #n=pd.to_numeric(column, errors='coerce')-1
    #return n.fillna(-99).astype(int).astype(str).str.replace('-99','')
    return column.replace({5: 4, 4: 3, 3: 2, 2: 1, 1: 0})


def __decrement_1_5_to_0_4_then_reverse_code(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale, reverse-coding where the manual calls for it, and recalculating scores accordingly."""
    #neo3=4-(pd.to_numeric(studydata.neo3,errors='coerce')-1)
    #studydata.neo3=neo3.fillna(-99).astype(int).astype(str).str.replace('-99','')
    return column.replace({5:0, 4: 1, 3: 2, 2: 3, 1: 4})

fn["neo1"]=__decrement_1_5_to_0_4
fn["neo2"]=__decrement_1_5_to_0_4
fn["neo3"]=__decrement_1_5_to_0_4_then_reverse_code
fn["neo4"]=__decrement_1_5_to_0_4
fn["neo5"]=__decrement_1_5_to_0_4
fn["neo6"]=__decrement_1_5_to_0_4
fn["neo7"]=__decrement_1_5_to_0_4
fn["neo8"]=__decrement_1_5_to_0_4_then_reverse_code
fn["neo9"]=__decrement_1_5_to_0_4
fn["neo10"]=__decrement_1_5_to_0_4
fn["neo11"]=__decrement_1_5_to_0_4
fn["neo12"]=__decrement_1_5_to_0_4
fn["neo13"]=__decrement_1_5_to_0_4
fn["neo14"]=__decrement_1_5_to_0_4
fn["neo15"]=__decrement_1_5_to_0_4
fn["neo16"]=__decrement_1_5_to_0_4
fn["neo17"]=__decrement_1_5_to_0_4
fn["neo18"]=__decrement_1_5_to_0_4
fn["neo19"]=__decrement_1_5_to_0_4
fn["neo20"]=__decrement_1_5_to_0_4
fn["neo21"]=__decrement_1_5_to_0_4
fn["neo22"]=__decrement_1_5_to_0_4
fn["neo23"]=__decrement_1_5_to_0_4
fn["neo24"]=__decrement_1_5_to_0_4
fn["neo25"]=__decrement_1_5_to_0_4
fn["neo26"]=__decrement_1_5_to_0_4
fn["neo27"]=__decrement_1_5_to_0_4
fn["neo28"]=__decrement_1_5_to_0_4
fn["neo29"]=__decrement_1_5_to_0_4_then_reverse_code
fn["neo30"]=__decrement_1_5_to_0_4
fn["neo31"]=__decrement_1_5_to_0_4
fn["neo32"]=__decrement_1_5_to_0_4
fn["neo33"]=__decrement_1_5_to_0_4
fn["neo34"]=__decrement_1_5_to_0_4
fn["neo35"]=__decrement_1_5_to_0_4
fn["neo36"]=__decrement_1_5_to_0_4
fn["neo37"]=__decrement_1_5_to_0_4
fn["neo38"]=__decrement_1_5_to_0_4_then_reverse_code
fn["neo39"]=__decrement_1_5_to_0_4
fn["neo40"]=__decrement_1_5_to_0_4
fn["neo41"]=__decrement_1_5_to_0_4
fn["neo42"]=__decrement_1_5_to_0_4
fn["neo43"]=__decrement_1_5_to_0_4
fn["neo44"]=__decrement_1_5_to_0_4
fn["neo45"]=__decrement_1_5_to_0_4
fn["neo46"]=__decrement_1_5_to_0_4
fn["neo47"]=__decrement_1_5_to_0_4
fn["neo48"]=__decrement_1_5_to_0_4
fn["neo49"]=__decrement_1_5_to_0_4
fn["neo50"]=__decrement_1_5_to_0_4
fn["neo51"]=__decrement_1_5_to_0_4
fn["neo52"]=__decrement_1_5_to_0_4
fn["neo53"]=__decrement_1_5_to_0_4
fn["neo54"]=__decrement_1_5_to_0_4
fn["neo55"]=__decrement_1_5_to_0_4
fn["neo56"]=__decrement_1_5_to_0_4
fn["neo57"]=__decrement_1_5_to_0_4
fn["neo58"]=__decrement_1_5_to_0_4
fn["neo59"]=__decrement_1_5_to_0_4
fn["neo60"]=__decrement_1_5_to_0_4

def dummy_var15(studydata, column, context):
    """Please use the 'version_form' column to label all rows "S7up Self Report"."""
    studydata['version_form']='S7up Self Report'
fn["dummy_var15"]=dummy_var15


fn["ale1_2"]=__increment_0_to_2
fn["ale2_2"]=__increment_0_to_2
fn["ale3_2"]=__increment_0_to_2
fn["ale4_2"]=__increment_0_to_2
fn["ale5_2"]=__increment_0_to_2
fn["ale6_2"]=__increment_0_to_2
fn["ale7_2"]=__increment_0_to_2
fn["ale8_2"]=__increment_0_to_2
fn["ale9_2"]=__increment_0_to_2
fn["ale10_2"]=__increment_0_to_2
fn["ale11_2"]=__increment_0_to_2
fn["ale12_2"]=__increment_0_to_2
fn["ale13_2"]=__increment_0_to_2
fn["ale14_2"]=__increment_0_to_2
fn["ale15_2"]=__increment_0_to_2
fn["ale16_2"]=__increment_0_to_2
fn["ale17_2"]=__increment_0_to_2
fn["ale18_2"]=__increment_0_to_2
fn["ale19_2"]=__increment_0_to_2
fn["ale20_2"]=__increment_0_to_2
fn["ale21_2"]=__increment_0_to_2
fn["ale22_2"]=__increment_0_to_2
fn["ale23_2"]=__increment_0_to_2
fn["ale24_2"]=__increment_0_to_2
fn["ale25_2"]=__increment_0_to_2

def dummy_var16(studydata, column, context):
    """Please use the 'version_form' column to label each row "Past year"."""
    studydata['version_form']='Past year'
fn["dummy_var16"]=dummy_var16

def nida_y_tobaco3(studydata, column, context):
    """Please recode 999 as 97."""
    return column.replace({999: 97})
fn["nida_y_tobaco3"]=nida_y_tobaco3

def nida_y_tobaco6b(studydata, column, context):
    """Please recode 3 as 2 and 6 as 3."""
    return column.replace({3: 2, 6: 3})
fn["nida_y_tobaco6b"]=nida_y_tobaco6b

def nida_y_tobaco7(studydata, column, context):
    """Please recode 1 as 2, 2 as 3, and 6 as 4."""
    return column.replace({
        1: 2,
        2: 3,
        6: 4,
    })
fn["nida_y_tobaco7"]=nida_y_tobaco7

def __recode_1_2_as_yes_no(studydata, column, context):
    """Please recode 1 as Yes and 2 as No."""
    return column.replace({
        1: 'Yes',
        2: 'No',
    })

fn["nida_y_drug1"]=__recode_1_2_as_yes_no
fn["nida_y_drug2"]=__recode_1_2_as_yes_no
fn["nida_y_drug3"]=__recode_1_2_as_yes_no
fn["nida_y_drug4"]=__recode_1_2_as_yes_no
fn["nida_y_drug5"]=__recode_1_2_as_yes_no
fn["nida_y_drug6"]=__recode_1_2_as_yes_no
fn["nida_y_drug7"]=__recode_1_2_as_yes_no
fn["nida_y_drug8"]=__recode_1_2_as_yes_no
fn["nida_y_drug9"]=__recode_1_2_as_yes_no
fn["nida_y_drug10"]=__recode_1_2_as_yes_no

def pds_sub_score(studydata, column, context):
    """Please split this column into two separate columns. Male participants' data can go to 'pds_pv_boy_tanner'. Female participants' data belong in 'pds_pv_girl_tanner'."""
    studydata['pds_pv_girl_tanner'] = column.where(studydata.gender=='F')
    studydata['pds_pv_boy_tanner'] = column.where(studydata.gender=='M')
fn["pds_sub_score"]=pds_sub_score

def mstrl_sub1a(studydata, column, context):
    """Please change numeric codes to the text strings they represent."""
    return column.replace({
        1: 'Hypothyroidism',
        2: 'No hypothyroidism'
    })
fn["mstrl_sub1a"]=mstrl_sub1a
fn["mstrl_sub1b"]=mstrl_sub1a #same logic as above

def __prepend_age_at_onset(studydata, column, context):
    """Please prepend "Age at onset: " to ages."""
    return column.mask(column.notna(), 'Age at onset: ' + column.astype(str))

fn["mstrl_sub1c_age"]=__prepend_age_at_onset

def dummy_var13(studydata, column, context):
    """Please indicate "Short Form" for each row using the column 'version_form'."""
    studydata['version_form']='Short Form'
fn["dummy_var13"]=dummy_var13

def dummy_var17(studydata, column, context):
    """Please indicate "Parent" for each row using the column 'version_form'."""
    studydata['version_form']='Parent'
fn["dummy_var17"]=dummy_var17

def srsa_total_raw(studydata, column, context):
    """Please split total raw scores by sex. Females' scores can go in 'female_rawscoreall'. Males' scores can go in 'male_rawscoreall'."""
    studydata['female_rawscoreall']=column.where(studydata.gender=='F')
    studydata['male_rawscoreall']=column.where(studydata.gender=='M')
fn["srsa_total_raw"]=srsa_total_raw

def dummy18(studydata, column, context):
    """Please split total raw scores by sex. Females' scores can go in 'female_rawscoreall'. Males' scores can go in 'male_rawscoreall'."""
    pass
fn["dummy18"]=dummy18

def srsa_total_tscore(studydata, column, context):
    """Please split total T-scores by sex. Males' scores can go in 'male_tscoreall'. Females' scores can go in 'female_tscoreall'."""
    studydata['female_tscoreall']=column.where(studydata.gender=='F')
    studydata['male_tscoreall']=column.where(studydata.gender=='M')
fn["srsa_total_tscore"]=srsa_total_tscore

def dummy19(studydata, column, context):
    """Please split total T-scores by sex. Males' scores can go in 'male_tscoreall'. Females' scores can go in 'female_tscoreall'."""
    pass
fn["dummy19"]=dummy19

def dummy_var1(studydata, column, context):
    """Please use the 'version_form' column to specify a time range of the "Self report, Past 6 months" for each row of data."""
    studydata['version_form']='Self report, Past 6 months'
fn["dummy_var1"]=dummy_var1

def dummy_var2(studydata, column, context):
    """Please fill all cells with 999 for this column, unless the respondent is known."""
    studydata['respond']='3'
fn["dummy_var2"]=dummy_var2

def dummy_var3(studydata, column, context):
    """Please fill all cells with 999 for this column, unless the respondent is known."""
    studydata['respond_detail']='999'
fn["dummy_var3"]=dummy_var3

def dummy_var4(studydata, column, context):
    """Please specify a cohort/group/diagnosis for participants in this column. If this is not applicable, then please fill each cell with 999."""
    studydata['phenotype']='999'
fn["dummy_var4"]=dummy_var4

def p_c_gender(studydata, column, context):
    """Please decrement values 1::6 to 0::5. Values of 7 and 8 can remain the same."""
    return column.replace({
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
    })
fn["p_c_gender"]=p_c_gender

fn["p_c_country"]=__convert_country_code_to_text

def p_gender(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    """Please combine 'p_gender_different' responses with those from 'p_gender' in a single column with either name."""
    return column.replace(CONST['gender']) + studydata.p_gender_different
fn["p_gender"]=p_gender

def p_race(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['race'])
fn["p_race"]=p_race
fn["p_country"]=__convert_country_code_to_text
fn["p_bio_f_country"]=__convert_country_code_to_text
fn["p_bio_m_county"]=__convert_country_code_to_text

def p_marriage(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['marriage_status'])
fn["p_marriage"]=p_marriage

def p_grade(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['education'])
fn["p_grade"]=p_grade

def p_job(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['working_status'])
fn["p_job"]=p_job

def ptner_grade(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    return column.replace(CONST['education'])
fn["ptner_grade"]=ptner_grade

def family_income(studydata, column, context):
    """Please convert the code of 999999 to -999999, as 999999 could be an actual value."""
    return column.replace({999999: -999999})
fn["family_income"]=family_income

def __increment_0_3_to_1_4(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    return column.replace({0:1, 1:2, 2:3, 3:4})

fn["psqi5a"]=__increment_0_3_to_1_4
fn["psqi5b"]=__increment_0_3_to_1_4
fn["psqi5c"]=__increment_0_3_to_1_4
fn["psqi5d"]=__increment_0_3_to_1_4
fn["psqi5e"]=__increment_0_3_to_1_4
fn["psqi5f"]=__increment_0_3_to_1_4
fn["psqi5g"]=__increment_0_3_to_1_4
fn["psqi5h"]=__increment_0_3_to_1_4
fn["psqi5i"]=__increment_0_3_to_1_4
fn["psqi5j_2"]=__increment_0_3_to_1_4

def devhx_8_prescript_med(studydata, column, context):
    """Please recode 0 as 999 (for "Don't Know")."""
    return column.replace({0:999})
fn["devhx_8_prescript_med"]=devhx_8_prescript_med

def devhx_9_prescript_med(studydata, column, context):
    """Please recode 0 as 999 (for "Don't Know")."""
    return column.replace({0:999})
fn["devhx_9_prescript_med"]=devhx_9_prescript_med

def pds_p_g5a(studydata, column, context):
    """Please recode 1 as 2 (for "No")."""
    return column.replace({1:2})
fn["pds_p_g5a"]=pds_p_g5a

def pds_p_mss_bcontrol(studydata, column, context):
    """Please recode 2 as 0 (for "No")."""
    return column.replace({2:0})
fn["pds_p_mss_bcontrol"]=pds_p_mss_bcontrol

def pds_p_score(studydata, column, context):
    """Please split this field between 'pds_pv_boy_tanner' for boys and 'pds_pv_girl_tanner' for girls."""
    studydata['pds_pv_girl_tanner'] = column.where(studydata.gender=='F')
    studydata['pds_pv_boy_tanner'] = column.where(studydata.gender=='M')
fn["pds_p_score"]=pds_p_score

def mstrl_p1a(studydata, column, context):
    """Please convert these numeric codes to the text strings they represent."""
    pass
fn["mstrl_p1a"]=mstrl_p1a

def mstrl_p1b(studydata, column, context):
    """Please convert these numeric codes to the text strings they represent."""
    pass
fn["mstrl_p1b"]=mstrl_p1b

def __prepend_onset(studydata, column, context):
    """Please prepend "Onset: " to ages."""
    return column.mask(column.notna(), 'Onset: ' + column.astype(str))

fn["mstrl_p1c_age"]=__prepend_onset

def __reverse_1_4_to_4_1(studydata, column, context):
    "Please reverse code this column. (Range: 1-4)"
    return column.replace({4:1, 3:2, 2:3, 1:4})
fn["upps_p1"]=__reverse_1_4_to_4_1
fn["upps_p2"]=__reverse_1_4_to_4_1
fn["upps_p4"]=__reverse_1_4_to_4_1
fn["upps_p7"]=__reverse_1_4_to_4_1
fn["upps_p8"]=__reverse_1_4_to_4_1
fn["upps_p11"]=__reverse_1_4_to_4_1
fn["upps_p12"]=__reverse_1_4_to_4_1
fn["upps_p13"]=__reverse_1_4_to_4_1
fn["upps_p14"]=__reverse_1_4_to_4_1
fn["upps_p17"]=__reverse_1_4_to_4_1
fn["upps_p18"]=__reverse_1_4_to_4_1
fn["upps_p20"]=__reverse_1_4_to_4_1
fn["upps_p21"]=__reverse_1_4_to_4_1
fn["upps_p26"]=__reverse_1_4_to_4_1
fn["upps_p27"]=__reverse_1_4_to_4_1
fn["upps_p28"]=__reverse_1_4_to_4_1
fn["upps_p29"]=__reverse_1_4_to_4_1
fn["upps_p30"]=__reverse_1_4_to_4_1
fn["upps_p31"]=__reverse_1_4_to_4_1
fn["upps_p32"]=__reverse_1_4_to_4_1
fn["upps_p33"]=__reverse_1_4_to_4_1
fn["upps_p34"]=__reverse_1_4_to_4_1
fn["upps_p35"]=__reverse_1_4_to_4_1
fn["upps_p36"]=__reverse_1_4_to_4_1
fn["upps_p37"]=__reverse_1_4_to_4_1
fn["upps_p38"]=__reverse_1_4_to_4_1
fn["upps_p39"]=__reverse_1_4_to_4_1
fn["upps_p40"]=__reverse_1_4_to_4_1

def medhx_1a(studydata, column, context):
    """Please keep data for these columns in their own rows, with 'version_form' labeling them "Past Year"."""
    pass
fn["medhx_1a"]=medhx_1a

def medhx_1a_other(studydata, column, context):
    """Please keep data for these columns in their own rows, with 'version_form' labeling them "Past Year"."""
    pass
fn["medhx_1a_other"]=medhx_1a_other

def medhx_6a_notes(studydata, column, context):
    """Please append " times" to each number."""
    return column.mask(column.notna(), column.astype(str) + ' times' )
fn["medhx_6a_notes"]=medhx_6a_notes


def hba1c(studydata, column, context):
    """When the quantity was not sufficient, please leave the cells blank rather than use a missing code."""
    pass
fn["hba1c"]=hba1c

