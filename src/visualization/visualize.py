import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

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

def winAfterWin(df, countries, asc=False):
    '''
    Calculates proportion of wins after a win in the previous match. Returns
    proportions as sorted dataframe with countries as index.
    '''
    win_props=[]
    for c in countries:
        data = df.query('country == @c')
        data.start_date = data.start_date.sort_values()
        data.reset_index(inplace=True)
        idx = data.index.values
        #Calcluate proportion of wins given previous win
        win_props.append((c, np.mean([(data.result[i+1]=="won")&(data.result[i]=="won") for i in idx[:-1]])))

    return pd.DataFrame(win_props).groupby(0, as_index=True).mean().sort_values(by=1, ascending=asc)

def winAfterLoss(df, countries, asc=False):
    '''
    Calculates proportion of wins after a loss in the previous match. Returns
    proportions as sorted dataframe with countries as index.
    '''
    win_props=[]
    for c in countries:
        data = df.query('country == @c')
        data.start_date = data.start_date.sort_values()
        data.reset_index(inplace=True)
        idx = data.index.values
        #Calcluate proportion of wins given previous win
        win_props.append((c, np.mean([(data.result[i+1]=="won")&(data.result[i]=="lost") for i in idx[:-1]])))

    return pd.DataFrame(win_props).groupby(0, as_index=True).mean().sort_values(by=1, ascending=False)
