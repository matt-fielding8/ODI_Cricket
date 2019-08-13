'''
All scripts for cleaning ODI data
'''

import pandas as pd

def formatHeaders(df):
    '''
    Rename all column headers lower case with whitespace removed.
    '''
    df.rename(lambda c: c.lower().replace(' ', '_'), axis=1, inplace=True)
