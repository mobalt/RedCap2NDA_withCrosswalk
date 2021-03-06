import inspect

# +
from code import fn

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
# **Note** that all the structures here in this particular crosswalk and release include data from parent database only _parent-about-child_  -- no _parent-about-parent_.
#
# parent about parent data to be dealt with later as extension of this release..i.e. with fu data, v2, and v3
# +
snapshotdate = datetime.datetime.today().strftime('%m_%d_%Y')

config = LoadSettings()
box = LifespanBox()
# -

crosswalk = pd.read_csv("HCPD-crosswalk.csv")
red = crosswalk[crosswalk.source == 'REDCap'].copy()

ndar = pd.read_csv('./UnrelatedHCAHCD_w_STG_Image_and_pseudo_GUID09_27_2019.csv')
ndar = ndar[ndar.subjectped.str.contains('HCD')]

structures = red.drop_duplicates('nda_structure')
normals = structures[structures.source.str.contains('REDCap') & structures.specialty_code.isnull()]

'Structures to traverse in for-loop: '+', '.join(normals.nda_structure)

cols_of_interest = ['nda_structure', 'nda_element', 'hcp_variable', 'source',
         'action_request', 'hcp_variable_upload', 'requested_python']

# # For-Loop

# +
for structure in normals.nda_structure:
    print(structure)

    current_structure = red[red.nda_structure == structure]
    variables = current_structure.hcp_variable.tolist()

    accumulator = []
    if current_structure.hcpdparent.any():
        studydata = get_behavioral('hcpdparent', ['child_id'] + variables)
        studydata = cw.parent2child(studydata)
        accumulator.append(studydata)
    if current_structure.hcpd18.any():
        studydata = get_behavioral('hcpd18', variables)
        accumulator.append(studydata)
    if current_structure.hcpdchild.any():
        studydata = get_behavioral('hcpdchild', variables)
        accumulator.append(studydata)
    studydata = pd.concat(accumulator)

#     if structure == 'vitals01':
#         studydata = cw.extraheightcleanvar(studydata)

    pathstructuresout = "./prepped_structures"
    studystr = 'hcpd'

    crosswalk_subset = crosswalk[crosswalk.hcp_variable.isin(variables)][cols_of_interest]

    for x, y in crosswalk_subset[['hcp_variable', 'hcp_variable_upload']].to_records(False):
        if not y:
            y = x
        if x in fn:
            # print({'name': x}, inspect.getsource(fn[x]))

            # handle dummy vars
            X = studydata[x] if x in studydata else None
            result = fn[x](studydata, X, {'name': x})
            if result is not None and y:
                studydata[y] = result
        elif x in studydata:
            studydata[y] = studydata[x]
        else:
            # dummy var doesn't actually exist as input
            pass


    # for livewire in crosswalk_subset.requested_python[crosswalk_subset.requested_python.notna()]:
    #     print(livewire)
    #     exec(livewire)


    # remove fields with empty values hcp_variable name in uploaded file
    #  (these are empty because NDA doesnt want them)
    crosswalk_subset = crosswalk_subset[crosswalk_subset['hcp_variable_upload'].notna()].reset_index()

    listout = ['subject'] + crosswalk_subset['hcp_variable_upload'].tolist()


    # merge with required fields from vars in intradb staging (guid, etc)
    # not sure whether it makes sense to pull these in here or recalculate on fly from redcap.
    # future issues:  compare this approach (e.g. pull from the file above named 'ndar') vs. what happens in the applycrosswalk.py
    # program for HCD, which regenerates on fly...will require some recodeing below to pull from redcap...
    # might just be easier to pull once...but how will this affect visit numbers?
    fields = {'nda_guid': 'subjectkey', 'subjectped': 'src_subject_id', 'nda_gender': 'gender',
            'nda_interview_date': 'interview_date', 'nda_interview_age': 'interview_age'}
    ndarsub = ndar[fields.keys()].rename(columns=fields).copy()

    dout = ndarsub.merge(studydata[listout], 'left', left_on='src_subject_id', right_on='subject').drop(columns='subject')
    dout.interview_date = dout.interview_date.astype('datetime64').dt.strftime('%m/%d/%Y')

#     filepath = f'{pathstructuresout}/HCPD_{structure}_{snapshotdate}.csv'
    filepath = f'{pathstructuresout}/HCPD_{structure}.csv'
    root, num = structure[:-2], structure[-2:]

    with open(filepath, 'w') as fd:
        fd.write('{},{:d}\n'.format(root, int(num)))
        dout.to_csv(fd, index=False)
# -


