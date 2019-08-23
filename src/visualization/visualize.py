import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
%matplotlib inline

def proportions(df, groupby=None, agg_method='count', agg_col='match_id', asc=False,
col1=None, filter1=None, col2=None, filter2=None):
    '''
    Filters df[col1] on filter1, df[col2] on filter2 and groups by group.
    Returns proportions as pd.series with filter1 as index.
    '''
    if agg_method == 'count':
        n_data = df[df[col1]==filter1].groupby(groupby).count()[agg_col]
        i_data = df[(df[col2]==filter2)&(df[col1]==filter1)].groupby(groupby).count()[agg_col]

    elif agg_method == 'mean':
        n_data = df[df[col1]==filter1].groupby(groupby).mean()[agg_col]
        i_data = df[(df[col1]==filter1)&(df[col2==filter2])].groupby(groupby).mean()[agg_col]

    return (i_data/n_data).sort_values(ascending=asc).dropna()
