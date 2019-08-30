import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def setPlot(figsize=[14.7,8.27],title="", xlabel="", ylabel="",
    axis_font=14, title_font=16, tick_font=14):
    '''
    Sets up matplotlib axis according to params. Returns None.
    '''
    _, ax = plt.subplots(figsize=figsize);
    ax.set_title(title, fontsize=title_font, fontweight='bold');
    ax.set_xlabel(xlabel, fontsize=axis_font);
    ax.set_ylabel(ylabel, fontsize=axis_font);
    plt.xticks(fontsize=tick_font);
    plt.yticks(fontsize=tick_font);

def setSeabornFigPlot(plot, w = 14.70, h = 8.27, title="", xlabel="", ylabel="",
    axis_font=14, title_font=16, title_pos = 1.04, tick_font=14):
    '''
    Sets up seaborn figure-level axis according to params. Returns None.
    '''
    plot.fig.set_figheight(h)
    plot.fig.set_figwidth(w)
    plot.set_xlabels(xlabel, fontsize = axis_font)
    plot.set_ylabels(ylabel, fontsize = axis_font)
    plot.fig.suptitle(title, fontsize = title_font, weight = "bold", y = title_pos);


def bins(df, var, manual=False, min=0, max=2, step=1):
    '''
    Creates bins using np.arange(). If manual=False use variable minimum and
    maximum values as bin edges, otherwise min and max parameters.
    '''
    if not manual:
        return np.arange(df[var].min(), df[var].max()+step, step)
    else:
        return np.arange(min, max+step, step)

def tickLabels(locs, multi=1, f=0, pcnt=False):
    ''' (list of int) -> list of str
    Return locs * multi as list of strings to i decimal places.
    '''
    if not pcnt:
        return ["{:0.{}f}".format(i*multi, f) for i in locs]
    else:
        return ["{:0.{}f}%".format(i*100, f) for i in locs]

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
