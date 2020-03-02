# +
import datetime
import json
import os
from io import BytesIO

import numpy as np
import pandas as pd
from libs.box import LifespanBox
from libs.config import LoadSettings

def parent2child(studydata):
    studydata = studydata \
        .drop(columns={'parent_id', 'subject', 'flagged'}) \
        .rename(columns={'child_id': 'subject_id'})
    new = studydata.subject_id.str.split("_", 1, expand=True)
    studydata['subject'] = new[0].str.strip()
    studydata['flagged'] = new[1].str.strip()
    return studydata


def Box2dataframe(curated_fileid_start):
    return box.Box2dataframe(curated_fileid_start)

pathout = './pathout/'
def redcap2structure(vars, crosswalk, pathstructuresout=pathout, studystr='hcpa', dframe=None):
    """
    Takes list of vars from the crosswalk, gets the data from Redcap, and puts into structure format after
    merging with NDAR requiredvars.  Outputs a csv structure in NDA format to pathstructureout location
    """
    if dframe is not None:
        studydata = dframe
    else:
        studydata = getredcapfieldsjson(fieldlist=vars, study=studystr)
    # get the relevant rows of the crosswalk
    # inner merge works for redcap source..need right merge for box, though, to get extra vars for missing people
    crosswalk_subset = \
        pd.merge(crosswalk, pd.DataFrame(vars, columns=['hcp_variable']), on='hcp_variable', how='inner')[
            ['nda_structure', 'nda_element', 'hcp_variable', 'source',
             'action_request',
             'hcp_variable name in uploaded file',
             'requested_python']]
    # execute transformation codes stored in the crosswalk
    for index, row in crosswalk_subset.iterrows():
        if pd.isna(row.requested_python):
            pass
        else:
            exec(row.requested_python)
    # remove fields with empty values hcp_variable name in uploaded file -- these are empty because NDA doesnt want them
    crosswalk_subset = crosswalk_subset.loc[crosswalk_subset['hcp_variable name in uploaded file'].notna()]
    listout = ['subject', 'flagged', 'interview_date', 'interview_age', 'gender'] + list(
        crosswalk_subset['hcp_variable name in uploaded file'])
    # output new variables and subset to those not flagged for withdrawal.
    transformed = studydata[listout].loc[studydata.flagged.isnull()].drop(
        columns={'flagged', 'interview_date', 'gender', 'interview_age'})
    # merge with required fields from vars in intradb staging (guid, etc)
    # not sure whether it makes sense to pull these in here or recalculate on fly from redcap.
    # future issues:  compare this approach (e.g. pull from the file above named 'ndar') vs. what happens in the applycrosswalk.py
    # program for HCD, which regenerates on fly...will require some recodeing below to pull from redcap...
    # might just be easier to pull once...but how will this affect visit numbers?
    ndarsub = ndar[['nda_guid', 'subjectped', 'nda_gender', 'nda_interview_age', 'nda_interview_date']].rename(
        columns={'nda_guid': 'subjectkey', 'subjectped': 'src_subject_id', 'nda_gender': 'gender',
                 'nda_interview_date': 'interview_date', 'nda_interview_age': 'interview_age'}).copy()
    dout = pd.merge(ndarsub, transformed, how='left', left_on='src_subject_id', right_on='subject').drop(
        columns='subject')
    dout['interview_date'] = pd.to_datetime(dout.interview_date).dt.strftime('%m/%d/%Y')
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


# use json format because otherwise commas in strings convert wrong in csv read
def getredcapfieldsjson(fieldlist, study):  # , token=token[0],field=field[0],event=event[0]):
    """
    Downloads requested fields from Redcap databases specified by details in redcapconfig file
    Returns panda dataframe with fields 'study', 'Subject_ID, 'subject', and 'flagged', where 'Subject_ID' is the
    patient id in the database of interest (sometimes called subject_id, parent_id) as well as requested fields.
    subject is this same id stripped of underscores or flags like 'excluded' to make it easier to merge
    flagged contains the extra characters other than the id so you can keep track of who should NOT be uploaded to NDA
    or elsewwhere shared
    """
    auth = pd.read_csv(redcapconfigfile)
    studydata = pd.DataFrame()
    fieldlistlabel = ['fields[' + str(i) + ']' for i in range(5, len(fieldlist) + 5)]
    fieldrow = dict(zip(fieldlistlabel, fieldlist))
    d1 = {'token': auth.loc[auth.study == study, 'token'].values[0], 'content': 'record', 'format': 'json',
          'type': 'flat',
          'fields[0]': auth.loc[auth.study == study, 'field'].values[0],
          'fields[1]': auth.loc[auth.study == study, 'interview_date'].values[0],
          'fields[2]': auth.loc[auth.study == study, 'sexatbirth'].values[0],
          'fields[3]': auth.loc[auth.study == study, 'sitenum'].values[0],
          'fields[4]': auth.loc[auth.study == study, 'dobvar'].values[0]}
    d2 = fieldrow
    d3 = {'events[0]': auth.loc[auth.study == study, 'event'].values[0], 'rawOrLabel': 'raw',
          'rawOrLabelHeaders': 'raw',
          'exportCheckboxLabel': 'false',
          'exportSurveyFields': 'false', 'exportDataAccessGroups': 'false', 'returnFormat': 'json'}
    data = {**d1, **d2, **d3}
    buf = BytesIO()
    ch = pycurl.Curl()
    ch.setopt(ch.URL, 'https://redcap.wustl.edu/redcap/srvrs/prod_v3_1_0_001/redcap/api/')
    ch.setopt(ch.HTTPPOST, list(data.items()))
    ch.setopt(ch.WRITEDATA, buf)
    ch.perform()
    ch.close()
    htmlString = buf.getvalue().decode('UTF-8')
    buf.close()
    d = json.loads(htmlString)
    pexpanded = pd.DataFrame(d)
    pexpanded = pexpanded.loc[~(pexpanded[auth.loc[auth.study == study, 'field'].values[0]] == '')]  ##
    new = pexpanded[auth.loc[auth.study == study, 'field'].values[0]].str.split("_", 1, expand=True)
    pexpanded['subject'] = new[0].str.strip()
    pexpanded['flagged'] = new[1].str.strip()
    pexpanded['study'] = study  # auth.study[i]
    studydata = pd.concat([studydata, pexpanded], axis=0, sort=True)
    studydata = studydata.rename(columns={auth.loc[auth.study == study, 'interview_date'].values[0]: 'interview_date'})
    # Convert age in years to age in months
    # note that dob is hardcoded var name here because all redcap databases use same variable name...sue me
    # interview date, which was originally v1_date for hcpd, has been renamed in line above, headerv2
    try:
        studydata['nb_months'] = (
                12 * (pd.to_datetime(studydata.interview_date).dt.year - pd.to_datetime(studydata.dob).dt.year) +
                (pd.to_datetime(studydata.interview_date).dt.month - pd.to_datetime(studydata.dob).dt.month) +
                (pd.to_datetime(studydata.interview_date).dt.day - pd.to_datetime(studydata.dob).dt.day) / 31)
        studydatasub = studydata.loc[studydata.nb_months.isnull()].copy()
        studydatasuper = studydata.loc[studydata.nb_months.notna()].copy()
        studydatasuper['nb_months'] = studydatasuper.nb_months.apply(np.floor).astype(int)
        studydatasuper['nb_monthsPHI'] = studydatasuper.nb_months
        studydatasuper.loc[studydatasuper.nb_months > 1080, 'nb_monthsPHI'] = 1200
        studydata = pd.concat([studydatasub, studydatasuper], sort=True)
        studydata = studydata.drop(columns={'nb_months'}).rename(columns={'nb_monthsPHI': 'interview_age'})
    except:
        pass
    # convert gender to M/F string
    try:
        studydata.gender = studydata.gender.str.replace('1', 'M')
        studydata.gender = studydata.gender.str.replace('2', 'F')
    except:
        print(study + ' has no variable named gender')
    return studydata


def extraheightcleanvar(dfnewchildold):
    dfnewchild = dfnewchildold.copy()
    dfnewchild.groupby('height').count()[0:50]
    dfnewchild['heightorig'] = dfnewchild.height
    dfnewchild.height = dfnewchild.height.str.lower().str.replace('"', "'")
    dfnewchild.height = dfnewchild.height.str.replace("''", "'")
    dfnewchild.loc[dfnewchild.height.str.contains('/') == True]
    dfnewchild.height = dfnewchild.height.str.replace("1/2", ".5")
    dfnewchild.height = dfnewchild.height.str.replace("ft'", "'")
    dfnewchild.height = dfnewchild.height.str.replace("ft", "'")
    dfnewchild.height = dfnewchild.height.str.replace("4,5'", "4'5'")
    dfnewchild.groupby('weight').count()[0:50]
    dfnewchild.weight = dfnewchild.weight.str.replace('lbs', '')
    dfnewchild.weight = dfnewchild.weight.str.replace(' LBS', '')
    dfnewchild.bpressure = dfnewchild.bpressure.str.replace('_', '')
    new = dfnewchild.height.str.split("'", n=1, expand=True)
    dfnewchild['heightfeet'] = new[0]
    dfnewchild['heightinch'] = new[1].str.replace("'", "")
    dfnewchild['heightinchnum'] = pd.to_numeric(dfnewchild.heightinch, errors='coerce')
    dfnewchild['heightfeetnum'] = pd.to_numeric(dfnewchild.heightfeet, errors='coerce')
    dfnewchild.loc[dfnewchild.heightinchnum.isnull() & (dfnewchild.height != ''), 'heightinchnum'] = 0
    dfnewchild['totalheightinches'] = 12 * dfnewchild.heightfeetnum + dfnewchild.heightinchnum
    # cleandata=dfnewchild.drop(columns=['height','heightorig','heightfeet', 'heightinch', 'heightinchnum', 'heightfeetnum']).copy()
    cleandata = dfnewchild[['bpressure', 'dob', 'flagged', 'gender', 'interview_age',
                            'interview_date', 'site', 'study', 'subject', 'subject_id', 'weight',
                            'totalheightinches']].copy()
    return cleandata


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

# will import the crosswalk and sort by structures, then do for all structures the following
# get fieldlist for items in this structure (if redcap based and not special case like session drugs)
# get the data from redcap corresponding to this fieldlist (sincerely hope no merging required with Box data...
# needs to be called study data because code snpts in crosswalk refer to studydata datafram
# structures=crosswalk.groupby('nda_structure').count().reset_index()[['nda_structure']]
structures = crosswalk.groupby('nda_structure').count().reset_index()[['nda_structure']]



structures = crosswalk.drop_duplicates('nda_structure')
# normal redcap structures
normals = structures[structures.source.str.contains('REDCap') & structures.specialty_code.isnull()]
normals

# +
crosswalk['dbasestring'] = crosswalk.dbase.astype(str)
crosswalk.loc[crosswalk.dbasestring.str.contains('hcp'), 'countdb'] = crosswalk.dbasestring.str.split().apply(len)

# note that all the structures here in this particular crosswalk and release include data from parent database only
# parent about child  -- no parent apbout parent.
# parent about parent data to be dealt with later as extension of this release..i.e. with fu data, v2, and v3
# -

normals

for structure in normals.nda_structure:
    elements = crosswalk.loc[crosswalk.nda_structure == structure][['hcp_variable']]
    vars = list(elements.hcp_variable)
    numstudies = crosswalk.loc[crosswalk.nda_structure == structure, 'countdb'].values[0]
    if numstudies == 1.0:
        study = crosswalk.loc[crosswalk.nda_structure == structure, 'dbase'].values[0]
        if study == 'hcpdparent':
            varsnew = ['child_id'] + vars
            studydata = getredcapfieldsjson(fieldlist=varsnew, study='hcpdparent')
            studydata = parent2child(studydata)  # put data in name of child (e.g. child_id becomes subject)
        else:
            studydata = getredcapfieldsjson(fieldlist=vars, study=study)
    if numstudies == 2.0:
        allstudydata = pd.DataFrame()
        studies = crosswalk.loc[crosswalk.nda_structure == structure, 'dbase'].values[0]
        for pop in studies.split():
            studydata = pd.DataFrame()
            if pop == 'hcpdparent':
                varsnew = ['child_id'] + vars
                studydata = getredcapfieldsjson(fieldlist=varsnew, study='hcpdparent')
                studydata = parent2child(studydata)  # put data in name of child (e.g. child_id becomes subject)
            else:
                studydata = getredcapfieldsjson(fieldlist=vars, study=pop)
            allstudydata = pd.concat([allstudydata, studydata], axis=0, sort=True)
        studydata = allstudydata.copy()
    # exceptions - no deviation from concat, but python snp too long to paste in column
    if structure == 'vitals01':
        studydata_v2 = extraheightcleanvar(studydata)
        studydata_v2.height = studydata_v2.totalheightinches
        studydata = studydata_v2.copy()
    redcap2structure(vars, crosswalk, pathstructuresout=pathout, studystr='hcpd', dframe=studydata)

# +
# special cases
#########   fenvs01 ##########################################
# fenvs01 requires a merge after two independent cats
# get vars from the hcpdchild and hcpd18 database
elements = crosswalk.loc[crosswalk.nda_structure == 'fenvs01'][['hcp_variable', 'specialty_code']]
elementscat = elements.loc[elements.specialty_code != '2']
varscat = list(elementscat.hcp_variable)
allstudydata = pd.DataFrame()
studies = crosswalk.loc[(crosswalk.nda_structure == 'fenvs01') & (crosswalk.specialty_code == '1'), 'dbase'].values[
    0]
# get and concatenate the frist set of fenvs vars associated with
for pop in studies.split():
    studydata = pd.DataFrame()
    studydata = getredcapfieldsjson(fieldlist=varscat, study=pop)
    allstudydata = pd.concat([allstudydata, studydata], axis=0, sort=True)
studydata = allstudydata

# get vars from the hcpd18 and hcpdparent databases
elementscat2 = elements.loc[elements.specialty_code == '2']
varscat2 = list(elementscat2.hcp_variable)
allstudydata2 = pd.DataFrame()
studies2 = crosswalk.loc[(crosswalk.nda_structure == 'fenvs01') & (crosswalk.specialty_code == '2'), 'dbase'].values[
    0]
# get and concatenate the frist set of fenvs vars associated with
for pop in studies2.split():
    studydata2 = pd.DataFrame()
    if pop == 'hcpdparent':
        varsnew = ['child_id'] + varscat2
        studydata2 = getredcapfieldsjson(fieldlist=varsnew, study='hcpdparent')
        studydata2 = parent2child(studydata2)  # put data in name of child (e.g. child_id becomes subject)
    else:
        studydata2 = getredcapfieldsjson(fieldlist=varscat2, study=pop)
    allstudydata2 = pd.concat([allstudydata2, studydata2], axis=0, sort=True)
studydata2 = allstudydata2
studydata2['fpnh_dad_count'] = studydata2.filter(regex="fpnh_dad___").astype(float).sum(axis=1)
studydata2['fpnh_mom_count'] = studydata2.filter(regex="fpnh_mom___").astype(float).sum(axis=1)
studydata2.loc[(studydata2.fpnh_dad_count > 1) & (studydata2.fpnh_dad___9.astype(str) == '1')][
    ['subject', 'site', 'subject_id', 'fpnh_dad_count', 'fpnh_mom_count']]
studydata2.loc[(studydata2.fpnh_mom_count > 1) & (studydata2.fpnh_mom___9.astype(str) == '1')][
    ['subject', 'site', 'subject_id', 'fpnh_dad_count', 'fpnh_mom_count']]

# translate checklist codes to strings and append - this is ugly code.  please dont judge
# dad
studydata2.loc[studydata2.fpnh_dad___1.astype(str) == '1', 'fpnh_dad___1'] = "Schizophrenia or Psychosis; "
studydata2.loc[studydata2.fpnh_dad___2.astype(str) == '1', 'fpnh_dad___2'] = "Depression; "
studydata2.loc[studydata2.fpnh_dad___3.astype(str) == '1', 'fpnh_dad___3'] = "Bipolar Disorder; "
studydata2.loc[studydata2.fpnh_dad___4.astype(str) == '1', 'fpnh_dad___4'] = "Anxiety that needed treatment; "
studydata2.loc[studydata2.fpnh_dad___5.astype(str) == '1', 'fpnh_dad___5'] = "Drug or Alcohol Problems; "
studydata2.loc[studydata2.fpnh_dad___6.astype(str) == '1', 'fpnh_dad___6'] = "Alzheimer's Disease or Dementia; "
studydata2.loc[studydata2.fpnh_dad___7.astype(str) == '1', 'fpnh_dad___7'] = "Parkinson's Disease; "
studydata2.loc[studydata2.fpnh_dad___8.astype(str) == '1', 'fpnh_dad___8'] = "Tourette's Syndrome; "
studydata2.loc[studydata2.fpnh_dad___9.astype(str) == '1', 'fpnh_dad___9'] = "NONE OF THE ABOVE; "

studydata2.loc[studydata2.fpnh_dad___1.astype(str) == '0', 'fpnh_dad___1'] = ""
studydata2.loc[studydata2.fpnh_dad___2.astype(str) == '0', 'fpnh_dad___2'] = ""
studydata2.loc[studydata2.fpnh_dad___3.astype(str) == '0', 'fpnh_dad___3'] = ""
studydata2.loc[studydata2.fpnh_dad___4.astype(str) == '0', 'fpnh_dad___4'] = ""
studydata2.loc[studydata2.fpnh_dad___5.astype(str) == '0', 'fpnh_dad___5'] = ""
studydata2.loc[studydata2.fpnh_dad___6.astype(str) == '0', 'fpnh_dad___6'] = ""
studydata2.loc[studydata2.fpnh_dad___7.astype(str) == '0', 'fpnh_dad___7'] = ""
studydata2.loc[studydata2.fpnh_dad___8.astype(str) == '0', 'fpnh_dad___8'] = ""
studydata2.loc[studydata2.fpnh_dad___9.astype(str) == '0', 'fpnh_dad___9'] = ""

studydata2['fpnh_dad'] = studydata2.fpnh_dad___1.astype(str) + studydata2.fpnh_dad___2.astype(str) \
                         + studydata2.fpnh_dad___3.astype(str) + studydata2.fpnh_dad___4.astype(str) \
                         + studydata2.fpnh_dad___5.astype(str) + studydata2.fpnh_dad___6.astype(str) \
                         + studydata2.fpnh_dad___7.astype(str) + studydata2.fpnh_dad___8.astype(str) \
                         + studydata2.fpnh_dad___9.astype(str)

studydata2['fpnh_dad'] = studydata2.fpnh_dad.str[:-2]

# mom
studydata2.loc[studydata2.fpnh_mom___1.astype(str) == '1', 'fpnh_mom___1'] = "Schizophrenia or Psychosis;"
studydata2.loc[studydata2.fpnh_mom___2.astype(str) == '1', 'fpnh_mom___2'] = "Depression; "
studydata2.loc[studydata2.fpnh_mom___3.astype(str) == '1', 'fpnh_mom___3'] = "Bipolar Disorder; "
studydata2.loc[studydata2.fpnh_mom___4.astype(str) == '1', 'fpnh_mom___4'] = "Anxiety that needed treatment; "
studydata2.loc[studydata2.fpnh_mom___5.astype(str) == '1', 'fpnh_mom___5'] = "Drug or Alcohol Problems; "
studydata2.loc[studydata2.fpnh_mom___6.astype(str) == '1', 'fpnh_mom___6'] = "Alzheimer's Disease or Dementia; "
studydata2.loc[studydata2.fpnh_mom___7.astype(str) == '1', 'fpnh_mom___7'] = "Parkinson's Disease; "
studydata2.loc[studydata2.fpnh_mom___8.astype(str) == '1', 'fpnh_mom___8'] = "Tourette's Syndrome; "
studydata2.loc[studydata2.fpnh_mom___9.astype(str) == '1', 'fpnh_mom___9'] = "NONE OF THE ABOVE; "

studydata2.loc[studydata2.fpnh_mom___1.astype(str) == '0', 'fpnh_mom___1'] = ""
studydata2.loc[studydata2.fpnh_mom___2.astype(str) == '0', 'fpnh_mom___2'] = ""
studydata2.loc[studydata2.fpnh_mom___3.astype(str) == '0', 'fpnh_mom___3'] = ""
studydata2.loc[studydata2.fpnh_mom___4.astype(str) == '0', 'fpnh_mom___4'] = ""
studydata2.loc[studydata2.fpnh_mom___5.astype(str) == '0', 'fpnh_mom___5'] = ""
studydata2.loc[studydata2.fpnh_mom___6.astype(str) == '0', 'fpnh_mom___6'] = ""
studydata2.loc[studydata2.fpnh_mom___7.astype(str) == '0', 'fpnh_mom___7'] = ""
studydata2.loc[studydata2.fpnh_mom___8.astype(str) == '0', 'fpnh_mom___8'] = ""
studydata2.loc[studydata2.fpnh_mom___9.astype(str) == '0', 'fpnh_mom___9'] = ""

studydata2['fpnh_mom'] = studydata2.fpnh_mom___1.astype(str) + studydata2.fpnh_mom___2.astype(str) \
                         + studydata2.fpnh_mom___3.astype(str) + studydata2.fpnh_mom___4.astype(str) \
                         + studydata2.fpnh_mom___5.astype(str) + studydata2.fpnh_mom___6.astype(str) \
                         + studydata2.fpnh_mom___7.astype(str) + studydata2.fpnh_mom___8.astype(str) \
                         + studydata2.fpnh_mom___9.astype(str)

studydata2['fpnh_mom'] = studydata2.fpnh_mom.str[:-2]

# merge them check issues
studydata2gether = pd.merge(studydata, studydata2[['subject', 'fpnh_dad', 'fpnh_mom']], how='outer', on='subject',
                            indicator=True)
# these two both withdrawn...inner merge okay
studydata2gether.loc[studydata2gether._merge == 'left_only'][['subject', 'site']]

# inner merge
studydata2gether = pd.merge(studydata, studydata2[['subject', 'fpnh_dad', 'fpnh_mom']], how='inner', on='subject')
# make structure
vars = varscat + varscat2
redcap2structure(vars, crosswalk, pathstructuresout=pathout, studystr='hcpd', dframe=studydata2gether)

######### end fenvs01 ##########################################

# +
# special case Penncnp
# +
extrasc = getredcapfieldsjson(fieldlist=[], study='hcpdchild')
extras18 = getredcapfieldsjson(fieldlist=[], study='hcpd18')
extras = pd.concat([extrasc, extras18], axis=0)

crosswalk_subset = crosswalk.loc[(crosswalk.source.str.contains('Box'))
                                 & (crosswalk.source.str.contains('PennCNP'))]

pennid = crosswalk_subset.dbase.unique()[0]
penn = Box2dataframe(pennid)
penn = penn.loc[penn.assessment == 'V1']

# execute any specialty codes
for index, row in crosswalk_subset.iterrows():
    if pd.isna(row.requested_python):
        pass
    else:
        exec(row.requested_python)

# create the two penncnp stuctures
structuresbox = crosswalk_subset.drop_duplicates(subset='nda_structure')[
    ['source', 'dbase', 'nda_structure', 'specialty_code']]
for structure in structuresbox.nda_structure:
    listvars = crosswalk_subset.loc[
        crosswalk_subset.nda_structure == structure, 'hcp_variable name in uploaded file'].tolist()
    pennstruct = penn[['subid'] + listvars]
    studydata = pd.merge(pennstruct, extras, left_on='subid', right_on='subject', how='right')
    transformed = studydata.loc[studydata.flagged.isnull()].drop(columns='flagged')
    # merge with required fields from ndar subjects
    # --age and date need be recalcuated on fly from redcap data because possiblity of multiple dates per person'
    ndarsub = ndar[['nda_guid', 'subjectped']].rename(
        columns={'nda_guid': 'subjectkey', 'subjectped': 'src_subject_id'}).copy()
    dout = pd.merge(ndarsub, transformed, how='left', left_on='src_subject_id', right_on='subject').drop(
        columns={'subject', 'dob', 'site', 'study', 'subject_id'})
    crosswalk_boxsubset = crosswalk_subset.loc[crosswalk_subset.nda_structure == structure]
    crosswalk_boxsubset.reset_index(inplace=True)
    strucroot = crosswalk_boxsubset.nda_structure.str.strip().str[:-2][0]
    strucnum = crosswalk_boxsubset.nda_structure.str.strip().str[-2:][0]
    filePath = os.path.join(pathout, 'HCPD_' + strucroot + strucnum + '_' + snapshotdate + '.csv')
    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        pass
        # print("Can not delete the file as it doesn't exists")
    with open(filePath, 'a') as f:
        f.write(strucroot + "," + str(int(strucnum)) + "\n")
        dout.to_csv(f, index=False)

###end penncnp
# -
# WISC,WPPSI,WAIS
# use extras from penn special case
for w in ['WISC', 'WPPSI', 'WAIS']:
    crosswalk_subset = crosswalk.loc[(crosswalk.source.str.contains('Box'))
                                     & (crosswalk.source.str.contains(w))]
    wid = crosswalk_subset.dbase.unique()[0]
    wisc = Box2dataframe(wid)
    wisc = wisc.loc[wisc.visit == 'V1']
    listvars = crosswalk_subset['hcp_variable name in uploaded file'].tolist()
    wiscstruct = wisc[['subject'] + listvars]
    studydata = pd.merge(wiscstruct, extras, left_on='subject', right_on='subject', how='right')
    transformed = studydata.loc[studydata.flagged.isnull()].drop(columns='flagged')
    # merge with required fields from ndar subjects
    # --age and date need be recalcuated on fly from redcap data because possiblity of multiple dates per person'
    ndarsub = ndar[['nda_guid', 'subjectped']].rename(
        columns={'nda_guid': 'subjectkey', 'subjectped': 'src_subject_id'}).copy()
    dout = pd.merge(ndarsub, transformed, how='left', left_on='src_subject_id', right_on='subject').drop(
        columns={'subject', 'dob', 'site', 'study', 'subject_id'})
    crosswalk_subset.reset_index(inplace=True)
    strucroot = crosswalk_subset.nda_structure.str.strip().str[:-2][0]
    strucnum = crosswalk_subset.nda_structure.str.strip().str[-2:][0]
    filePath = os.path.join(pathout, 'HCPD_' + strucroot + strucnum + '_' + snapshotdate + '.csv')
    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        pass
        # print("Can not delete the file as it doesn't exists")
    with open(filePath, 'a') as f:
        f.write(strucroot + "," + str(int(strucnum)) + "\n")
        dout.to_csv(f, index=False)

# +
# caffeine nicotine and other drug sessions
# need six rows per person corresponding to 6 sessions
# +
crosswalk_subset = crosswalk.loc[crosswalk.nda_structure == 'drugscr01']
sessions = ['1', '2', '3', '4', '5', '6']
renamelist = crosswalk_subset.loc[(crosswalk_subset.hcp_variable.str.contains('s1') == True) |
                                  (crosswalk_subset.hcp_variable.str.contains(
                                      'drug1') == True), 'hcp_variable'].tolist() + ['alc_breath1']
allsessions = pd.DataFrame()
for session in sessions:
    slist = crosswalk_subset.loc[(crosswalk_subset.hcp_variable.str.contains('s' + session) == True) |
                                 (crosswalk_subset.hcp_variable.str.contains(
                                     'drug' + session) == True), 'hcp_variable'].tolist() + ['alc_breath' + session]
    allstudydata = pd.DataFrame()
    studies = crosswalk_subset.dbase.values[0]
    for pop in studies.split():
        studydata = pd.DataFrame()
        studydata = getredcapfieldsjson(fieldlist=slist, study=pop)
        allstudydata = pd.concat([allstudydata, studydata], axis=0, sort=True)
    allstudydata['caffeine_s' + session + '___1'] = allstudydata['caffeine_s' + session + '___1'].str.replace('1',
                                                                                                              'Prior to visit')
    allstudydata['caffeine_s' + session + '___2'] = allstudydata['caffeine_s' + session + '___2'].str.replace('2',
                                                                                                              'During visit')
    allstudydata['caffeine_s' + session] = allstudydata['caffeine_s' + session + '___1'] + ' ' + allstudydata[
        'caffeine_s' + session + '___2']
    allstudydata['caffeine_s' + session] = allstudydata['caffeine_s' + session].str.replace('0', '')
    allstudydata['nicotine_s' + session + '___1'] = allstudydata['nicotine_s' + session + '___1'].str.replace('1',
                                                                                                              'Prior to visit')
    allstudydata['nicotine_s' + session + '___2'] = allstudydata['nicotine_s' + session + '___2'].str.replace('2',
                                                                                                              'During visit')
    allstudydata['nicotine_s' + session] = allstudydata['nicotine_s' + session + '___1'] + ' ' + allstudydata[
        'nicotine_s' + session + '___2']
    allstudydata['nicotine_s' + session] = allstudydata['nicotine_s' + session].str.replace('0', '')
    allstudydata = allstudydata.drop(
        columns=['caffeine_s' + session + '___1', 'caffeine_s' + session + '___2', 'nicotine_s' + session + '___1',
                 'nicotine_s' + session + '___2']).copy()
    varmap = dict(zip(slist, renamelist))
    allstudydata = allstudydata.rename(columns=varmap)
    allstudydata['version_form'] = session
    allsessions = pd.concat([allsessions, allstudydata], axis=0, sort=True)

lout = list(crosswalk_subset['hcp_variable name in uploaded file'])
cleanedlist = [x for x in lout if str(x) != 'nan']
listout = ['subject', 'flagged', 'interview_date', 'interview_age',
           'gender'] + cleanedlist  # output new variables and subset to those not flagged for withdrawal.
transformed = allsessions[listout].loc[allsessions.flagged.isnull()].drop(
    columns={'flagged', 'interview_date', 'gender', 'interview_age'})
# merge with required fields from vars in intradb staging (guid, etc)
# not sure whether it makes sense to pull these in here or recalculate on fly from redcap.
# future issues:  compare this approach (e.g. pull from the file above named 'ndar') vs. what happens in the applycrosswalk.py
# program for HCD, which regenerates on fly...will require some recodeing below to pull from redcap...
# might just be easier to pull once...but how will this affect visit numbers?
ndarsub = ndar[['nda_guid', 'subjectped', 'nda_gender', 'nda_interview_age', 'nda_interview_date']].rename(
    columns={'nda_guid': 'subjectkey', 'subjectped': 'src_subject_id', 'nda_gender': 'gender',
             'nda_interview_date': 'interview_date', 'nda_interview_age': 'interview_age'}).copy()
dout = pd.merge(ndarsub, transformed, how='left', left_on='src_subject_id', right_on='subject').drop(columns='subject')
dout['interview_date'] = pd.to_datetime(dout.interview_date).dt.strftime('%m/%d/%Y')
# now export
crosswalk_subset.reset_index(inplace=True)
strucroot = crosswalk_subset.nda_structure.str.strip().str[:-2][0]
strucnum = crosswalk_subset.nda_structure.str.strip().str[-2:][0]
# finalsubset - i.e. no withdraws
# subjectkey	src_subject_id	interview_age	interview_date	gender
filePath = os.path.join(pathout, 'HCPD_' + strucroot + strucnum + '_' + snapshotdate + '.csv')
if os.path.exists(filePath):
    os.remove(filePath)
else:
    pass
    # print("Can not delete the file as it doesn't exists")

    with open(filePath, 'a') as f:
        f.write(strucroot + "," + str(int(strucnum)) + "\n")
        dout.to_csv(f, index=False)

# +
###notes for when the bloodsamples and labs come in for hcd (different than hca_
# child	bld_hba1c = hcpd18	hba1c
# hcpd18	bld_rucdr_saliva = child	rucdrsaliva
# not requested: hcpd18	blood_notes, child	external_notes, and child	rucdrsaliva_note, and  hcpd18	salisaliva_collectdt
