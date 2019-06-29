## Code for cleaning data

# Rename column script, lower case and whitespace
def renameCols(df):
    '''
    Rename all column headers lower case with whitespace removed.
    '''
    df.rename(lambda c: c.lower().replace(' ', '_'), axis=1, inplace=True)

# Replace string type data with NaN
def replaceNaN (df, col_list, str):
    ''' (df, list of str, str) -> df
    Replace values equal to str in df[col_list] with NaN.
    '''
    for col in col_list:
        df[col] = np.where(df[col] == str, np.NaN, df[col])

# Count instances of str in each column
def countVal (df, s):
    ''' (df, str) -> list of dct
    Counts instances of s for each column in df with type object. Returns counts for each column
    as a list of dct.
    '''
    return [{c:(df[c].str.count('(^)'+s+'($)')).sum()} for c in df.loc[:, df.dtypes==object].columns]

# Make no result values common
def noResult(df, col, lst, new_val):
    '''
    For df['col'], make all values in lst equal to new_val.
    '''
    for val in lst:
        df[col].replace(lst, new_val, inplace=True)

# Split winning margin column
def splitCol(df, col, new_col1, new_col2):
    '''
    Extracts numerical digits in df[col] into new_col1 then converts them to
    type float. Extarcts alphabetical chars from df[col] into new_col2.
    '''
    df[new_col1] = df.margin.str.extract('(\d+)').astype(float)
    df[new_col2] = df.margin.str.extract('([a-zA-Z]+)')
    df.drop(col, axis=1, inplace=True)

# Remove match_id prefix
def matchPrefix(df, col):
    '''
    Extract only digits from each value in df[col] as int and reassign to df[col]
    '''
    df[col] = df[col].str.extract('(\d+)').astype(int)

# Remove oppositon prefix
def oppPrefix(df, col):
    '''
    Remove first 3 chars from each value in df[col]
    '''
    df[col] = df[col].str[2:]

def dupIndex(df, col):
    ''' (df, str)->list of int
    Returns index values for all duplicate values in df[col] not including
    the 1st instance.
    ''''
    return np.array(df[df[col].duplicated].index)

# Change object types to float.
def toFloat(df, col_list):
    '''
    Change data types in col_list to type float.
    '''
    for col in col_list:
        df[col] = df[col].astype(float)
