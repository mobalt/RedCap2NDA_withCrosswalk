
def parent2child(df):
    df = df\
        .drop(columns=['subjectid'])\
        .rename(columns={'child_id': 'subjectid'})

    df[['subject','flagged']] = df.subjectid.str.split('_', 1, expand=True)
    return df

def extraheightcleanvar(dfnewchildold):
    dfnewchild = dfnewchildold.copy()
    h = dfnewchild.height.str.extract('^(?P<feet>[0-9.]+)(?:[^0-9.]+(?P<inches>[0-9.]+))?')
    dfnewchild.height = 12*h.feet.astype(float) + h.inches.astype(float)
    dfnewchild.height = dfnewchild.height.fillna(0)
    if dfnewchild.weight.dtype == 'object':
        dfnewchild.weight = dfnewchild.weight.str.extract('([0-9.]+)', expand=False).astype(float)

    dfnewchild.bpressure = dfnewchild.bpressure.str.replace('_', '')

    cleandata = dfnewchild[['bpressure', 'dob', 'flagged', 'gender', 'interview_age',
                            'interview_date', 'site', 'study', 'subject', 'subjectid', 'weight',
                            'height']].copy()
    return cleandata

pathout = './pathout/'
def redcap2structure(variables, crosswalk, pathstructuresout=pathout, studystr='hcpa', dframe=None):
    """ Takes list of vars from the crosswalk, gets the data from Redcap, and puts into structure format after
    merging with NDAR requiredvars.  Outputs a csv structure in NDA format to pathstructureout location
    """
    if dframe is not None:
        studydata = dframe
    else:
        studydata = get_behavioral(studystr, variables)
    # get the relevant rows of the crosswalk
    crosswalk_subset = crosswalk[crosswalk.hcp_variable.isin(variables)]\
        [['nda_structure', 'nda_element', 'hcp_variable', 'source',
         'action_request', 'hcp_variable_upload', 'requested_python']]

    # execute transformation codes stored in the crosswalk
    # TODO: sanitize input to prevent malicious code injection
    for livewire in crosswalk_subset.requested_python[crosswalk_subset.requested_python.notna()]:
        print(livewire)
        exec(livewire)

    # remove fields with empty values hcp_variable name in uploaded file -- these are empty because NDA doesnt want them
    crosswalk_subset = crosswalk_subset[crosswalk_subset['hcp_variable_upload'].notna()]
    listout = ['subject', 'flagged', 'interview_date', 'interview_age', 'gender'] +\
                crosswalk_subset['hcp_variable_upload'].tolist()
    # output new variables and subset to those not flagged for withdrawal.
    transformed = studydata[listout][studydata.flagged.isnull()].drop(
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
