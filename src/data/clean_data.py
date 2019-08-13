'''
All scripts for cleaning ODI data
'''

import pandas as pd
import numpy as np

def formatHeaders(df):
    '''
    Rename all column headers lower case with whitespace removed.
    '''
    df.rename(lambda c: c.lower().replace(' ', '_'), axis=1, inplace=True)

def renameCols(df, old_name_list, new_name_list):
    '''
    Replace columns in old_name_list with names in new_name_list.
    Pre-condition: len(old_name_list) == len(new_name_list)
    '''
    for i in range(len(old_name_list)):
        df.rename(columns={old_name_list[i]:new_name_list[i]}, inplace=True)

def replaceNaN (df, col_list, str):
    ''' (df, list of str, str) -> df
    Replace values equal to str in df[col_list] with NaN.
    '''
    for col in col_list:
        df[col] = np.where(df[col] == str, np.NaN, df[col])
