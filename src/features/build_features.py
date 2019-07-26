## Code for cleaning data

# Rename column script, lower case and whitespace
def renameCols(df):
    '''
    Rename all column headers lower case with whitespace removed.
    '''
    df.rename(lambda c: c.lower().replace(' ', '_'), axis=1, inplace=True)

#Rename columns
def renameCols2(df, old_name_list, new_name_list):
    '''
    Rename columns in old_name_list with names in new_name_list.
    Pre-condition: len(old_name_list) == len(new_name_list)
    '''
    for i in range(len(old_name_list)):
        df.rename(columns={old_name_list[i]:new_name_list[i]}, inplace=True)

def renameCols3(df, suffix):
    '''
    Add suffix to every column name in df.
    '''
    df.rename(lambda c: c + suffix, axis=1, inplace=True)

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

# Merge validation
def checkMerge(df, col_list1, col_list2):
    '''
    Checks equality between columns in col_list1 and col_list2 in df.
    Precondition: len(col_list1) == len(col_list2)
    '''
    for i in range(len(col_list1)):
        try:
            assert((df[col_list1[i]] != df[col_list2[i]]).sum() == 0)
        except:
            print("AssertionError:", col_list1[i], "!=", col_list2[i])

# Gather missing match data
def getScoreData(url):
    ''' str -> dct
    Uses requests and bs4 libraries to extract and parse html data from url.
    Returns a dct with 'team' and 'score' indices.
    '''
    score_lst = []
    team_lst=[]

    r = requests.get(url)
    # Create .txt file and write html content
    with open(os.path.join('../Data/raw/espn_html/', url.split('/')[-1] + ".txt"), mode='wb') as f:
        f.write(r.content)

    # Extract team and score data from .txt file
    with open(os.path.join('../Data/raw/espn_html/', url.split('/')[-1] + ".txt")) as f:
        soup = BeautifulSoup(f, 'lxml')
        score = soup.find_all(class_='cscore_score')
        team = soup.find_all(class_='cscore_name--long')

    # Write content to dct
    for i in range(len(score)//2):
        score_lst.append(score[i].contents[0])
        team_lst.append(team[i].contents[0])
        score_dct = {'team':team_lst, 'score':score_lst}

    return score_dct

def getSoup(url):
    '''
    Creates a response object using requests library and returns a soup in
    bytes format for a given url.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup
