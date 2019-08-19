'''
All scripts for cleaning ODI data
'''

import pandas as pd
import numpy as np
import re

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

def replaceNaN (df,  str):
    ''' (df, str) -> df
    Replace values of str with NaN for each column wih type object.
    '''
    for col in df.loc[:, df.dtypes==object].columns:
        df[col] = np.where(df[col] == str, np.NaN, df[col])

def countVal (df, s):
    ''' (df, str) -> list of dct
    Counts instances of s for each column in df with type object. Returns counts for each column
    as a list of dct.
    '''
    return [{c:(df[c].str.count('(^)'+s+'($)')).sum()} for c in df.loc[:, df.dtypes==object].columns]

def commonValue(df, col, lst, new_val):
    '''
    For df['col'], make all values in lst equal to new_val.
    '''
    for val in lst:
        df[col].replace(lst, new_val, inplace=True)

def splitCol(df, col, new_col1, new_col2):
    '''
    Extracts numerical digits in df[col] into new_col1 then converts them to
    type float. Extracts alphabetical chars from df[col] into new_col2.
    Drops df[col].
    '''
    df[new_col1] = df.margin.str.extract('(\d+)').astype(float)
    df[new_col2] = df.margin.str.extract('([a-zA-Z]+)')
    df.drop(col, axis=1, inplace=True)

def matchPrefix(df, col):
    '''
    Extract only digits from each value in df[col] as str and reassign to df[col]
    '''
    df[col] = df[col].str.extract('(\d+)')

def splitUpper(x):
    '''
    Inserts a space before capital letters in string x.
    >>> splitUpper("WestIndies"):
    "West Indies"
    '''
    split = re.findall('[A-Z][^A-Z]*', x)
    string = ""
    for s in split:
        string = string + s + " "

    return string.strip()
