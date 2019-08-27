"""
All the scripts required to gather missing data from
https://www.espncricinfo.com/
"""
from bs4 import BeautifulSoup
import requests
import numpy as np

def getSoup(url):
    '''
    Returns soup for url response object.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def getMatchid(soup):
    ''' (html) -> list of str
    Return match_id as list of string from soup.
    '''
    try:
        return soup.find(lambda tag: tag.name == 'a' and 'ODI no' in tag.get_text()).contents
    except Exception as e:
        print("Match ID Extraction Error\n", e, '\n', url)
        return ['-']

# Gather missing score data
def getMissingData(url):
    ''' str -> dct
    Uses requests and bs4 libraries to extract and parse html data from url.
    Returns a dct with 'match_id', 'country', 'score', 'detailed_score' keys.
    '''
    soup = getSoup(url)
    # Extract match_id
    try:
        match_id = soup.find(lambda tag: tag.name == 'a' and 'ODI no' in tag.get_text()).contents
    except Exception as e:
        print("Match ID Extraction Error\n", e, '\n', url)
        match_id = [np.NaN]
    print(match_id)
    # Extract score data from soup
    score = soup.find_all(class_='cscore_score')
    try:
        score_lst = [i.contents[0] for i in score]
    except Exception as e:
        print("Score Extraction Error\n", e, '\n', match_id, url)
        score_lst = [np.NaN]*2
    # Extract country data from soup
    country = soup.find_all(class_='cscore_name--long')
    try:
        country_lst =  [i.contents[0] for i in country]
    except Exception as e:
        print("Country Extraction\n", e, '\n', e, url)
        country_lst = [np.NaN]*2
    # Extract detailed score data from soup
    ## Find tags containg "TOTAL"
    tot_tags = soup.find_all(lambda tag: tag.name == 'div' and \
        tag.get('class')==['cell'] and tag.get_text()=='TOTAL')
    if len(tot_tags) == 2:
        try:
            detailed_score = [i.findNext().contents[0] for i in tot_tags]
        except Exception as e:
            print("detailed_score Extraction Error\n", e, '\n', url)
            detailed_score = [np.NaN]*2

    else:
        print("No result likely", url)
        detailed_score = [np.NaN]*2
    # Write information to dct
    score_dct = {'match_id':match_id*2,
                'country':country_lst[:2],
                'score':score_lst[:2],
                'detailed_score':detailed_score}

    return score_dct

# Get page links directing to all results per year
def yearPageLinks(soup):
    ''' wb -> list of str
    Extracts relative links in "QuoteSummary" class from soup.
    Returns relative url's as a list of str.
    '''
    link_list = []
    try:
        for i in soup.find_all(class_='QuoteSummary'):
            link_list.append(i['href'])
    except:
        print('Class "QuoteSummary" does not exist')

    return link_list

# Filter links based on criteria
def filterLinks(links, lst):
    """ (list of str, list of str) -> list of str
    Filters elements in links which contain elements in lst as a substring.
    Returns filtered elements as a list.
    """
    filt_links = ([(list(filter(lambda x: i in x, links))) for i in lst])
    # Flatten filt_links list
    return [i for link in filt_links for i in link]

# Turn relative url to absolute using prefix
def absoluteUrl(prefix, relative):
    '''
    Joins prefix with relative. Returns an absolute url.
    '''
    prefix = prefix.rstrip('/')
    return [prefix + link for link in relative]

# Get scorecard links
def scorecardLinks(year_links, match_ids):
    ''' (lst of str, list of str) -> list of str
    Loops through year_links and returns a list of relative links for all
    id's in match_ids.
    '''
    # Generate soup for all year_links
    soups = [getSoup(link) for link in year_links]
    # Retrieve all links within each soup
    raw_links = [soup.find_all(['tr', 'td','a'], class_=['data-link'], attrs=['href']) for soup in soups]

    # Extract all links associated with elements in match_ids
    sc_links_found = []
    for year_page in raw_links:
        for link in year_page:
            if link.contents[0] in match_ids:
                sc_links_found.append(link['href'])

    return sc_links_found

def flattenList(lst):
    ''' (lst of lst) -> lst
    Flattens elements of lst.
    '''
    return [j for i in lst for j in i]
