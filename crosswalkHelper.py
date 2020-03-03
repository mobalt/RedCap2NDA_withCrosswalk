
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
    dfnewchild.weight.str.extract('([0-9.]+)', expand=False).astype(float)

    dfnewchild.bpressure = dfnewchild.bpressure.str.replace('_', '')

    cleandata = dfnewchild[['bpressure', 'dob', 'flagged', 'gender', 'interview_age',
                            'interview_date', 'site', 'study', 'subject', 'subjectid', 'weight',
                            'height']].copy()
    return cleandata

