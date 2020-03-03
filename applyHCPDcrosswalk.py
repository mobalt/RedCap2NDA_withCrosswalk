# +
import datetime
import json
import os
from io import BytesIO

import crosswalkHelper as cw
import numpy as np
import pandas as pd
from libs.box import LifespanBox
from libs.config import LoadSettings
from libs.redcap import RedcapTable, get_behavioral_ids, get_behavioral



# +
box = LifespanBox()

snapshotdate = datetime.datetime.today().strftime('%m_%d_%Y')

###REDCAP API tokens moved to configuration file
config = LoadSettings()
boxconfigfile = config['box']
# -

crosswalkfile = "HCPD-crosswalk.csv"
crosswalk = pd.read_csv(crosswalkfile)

ndar = pd.read_csv('./UnrelatedHCAHCD_w_STG_Image_and_pseudo_GUID09_27_2019.csv')
ndar = ndar[ndar.subjectped.str.contains('HCD')]

pathout = "./prepped_structures"

structures = crosswalk.drop_duplicates('nda_structure')
# normal redcap structures
normals = structures[structures.source.str.contains('REDCap') & structures.specialty_code.isnull()]

# +
crosswalk['dbasestring'] = crosswalk.dbase.astype(str)
crosswalk.loc[crosswalk.dbasestring.str.contains('hcp'), 'countdb'] = crosswalk.dbasestring.str.split().apply(len)

# note that all the structures here in this particular crosswalk and release include data from parent database only
# parent about child  -- no parent apbout parent.
# parent about parent data to be dealt with later as extension of this release..i.e. with fu data, v2, and v3
# -
normals.nda_structure

for structure in normals.nda_structure.tolist()[:]:
    current_structure = crosswalk[crosswalk.nda_structure == structure]
    variables = current_structure.hcp_variable.tolist()
    numstudies = current_structure.countdb.values[0]
    if numstudies == 1.0:
        study = current_structure.dbase.values[0]
        if study == 'hcpdparent':
            varsnew = ['child_id'] + variables
            studydata = get_behavioral(study, varsnew)
            studydata = cw.parent2child(studydata)  # put data in name of child (e.g. child_id becomes subject)
        else:
            studydata = get_behavioral(study, variables)
    if numstudies == 2.0:
        allstudydata = pd.DataFrame()
        studies = current_structure.dbase.values[0]
        for study in studies.split():
            studydata = pd.DataFrame()
            if study == 'hcpdparent':
                varsnew = ['child_id'] + variables
                studydata = get_behavioral(study, varsnew)
                studydata = cw.parent2child(studydata)  # put data in name of child (e.g. child_id becomes subject)
            else:
                studydata = get_behavioral(study, variables)
            allstudydata = pd.concat([allstudydata, studydata], axis=0, sort=True)
        studydata = allstudydata.copy()
    # exceptions - no deviation from concat, but python snp too long to paste in column
    if structure == 'vitals01':
        studydata_v2 = cw.extraheightcleanvar(studydata)
        studydata = studydata_v2.copy()

    redcap2structure(variables, crosswalk, pathstructuresout=pathout, studystr='hcpd', dframe=studydata)

pathstructuresout = pathout
studystr = 'hcpd'
dframe = studydata

# 1. Takes list of vars from the crosswalk
# 2. gets the data from Redcap
# 3. puts into structure format after merging with NDAR requiredvars
# 4. Outputs a csv structure in NDA format

crosswalk_subset = crosswalk[crosswalk.hcp_variable.isin(variables)]\
        [['nda_structure', 'nda_element', 'hcp_variable', 'source',
         'action_request', 'hcp_variable_upload', 'requested_python']]

for livewire in crosswalk_subset.requested_python[crosswalk_subset.requested_python.notna()]:
    exec(livewire)

# remove fields with empty values hcp_variable name in uploaded file -- these are empty because NDA doesnt want them
crosswalk_subset = crosswalk_subset[crosswalk_subset['hcp_variable_upload'].notna()]
listout = ['subject', 'flagged', 'interview_date', 'interview_age', 'gender'] + crosswalk_subset['hcp_variable_upload'].tolist()

# output new variables and subset to those not flagged for withdrawal.
transformed = studydata[listout][studydata.flagged.isnull()].drop(
    columns={'flagged', 'interview_date', 'gender', 'interview_age'})

# merge with required fields from vars in intradb staging (guid, etc)
# not sure whether it makes sense to pull these in here or recalculate on fly from redcap.
# future issues:  compare this approach (e.g. pull from the file above named 'ndar') vs. what happens in the applycrosswalk.py
# program for HCD, which regenerates on fly...will require some recodeing below to pull from redcap...
# might just be easier to pull once...but how will this affect visit numbers?
ndarsub = ndar[['nda_guid', 'subjectped', 'nda_gender', 'nda_interview_age', 'nda_interview_date']]\
    .rename(columns={'nda_guid': 'subjectkey', 'subjectped': 'src_subject_id', 'nda_gender': 'gender',
             'nda_interview_date': 'interview_date', 'nda_interview_age': 'interview_age'}).copy()
dout = pd.merge(ndarsub, transformed, how='left', left_on='src_subject_id', right_on='subject')\
        .drop(columns='subject')
dout['interview_date'] = pd.to_datetime(dout.interview_date).dt.strftime('%m/%d/%Y')

# +
# now export
crosswalk_subset.reset_index(inplace=True)
strucroot = crosswalk_subset.nda_structure.str.strip().str[:-2][0]
strucnum = crosswalk_subset.nda_structure.str.strip().str[-2:][0]
# finalsubset - i.e. no withdraws
# subjectkey	src_subject_id	interview_age	interview_date	gender
filePath = os.path.join(pathstructuresout, 'HCPD_' + strucroot + strucnum + '_' + snapshotdate + '.csv')
if os.path.exists(filePath):
    os.remove(filePath)
else:
    pass
    # print("Can not delete the file as it doesn't exists")

with open(filePath, 'a') as f:
    f.write(strucroot + "," + str(int(strucnum)) + "\n")
    dout.to_csv(f, index=False)
# -
























studydata.columns[studydata.columns.str.contains('___')]

studydata_v2.columns











