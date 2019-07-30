"""
All the scripts required to gether missing data from
https://www.espncricinfo.com/
"""
from bs4 import BeautifulSoup
import requests

class Gather:
    def getSoup(self, url):
        '''
        Returns soup for url response object.
        '''
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup

    # Gather missing score data
    def getScoreData(self, url):
        ''' str -> dct
        Uses requests and bs4 libraries to extract and parse html data from url.
        Returns a dct with 'team' and 'score' indices.
        '''
        soup = getSoup(url)
        # Extract team and score data from soup
        score = soup.find_all(class_='cscore_score')
        team = soup.find_all(class_='cscore_name--long')

        # Write scores for both teams to dct
        score_lst = []
        team_lst=[]
        for i in range(len(score)//2):
            score_lst.append(score[i].contents[0])
            team_lst.append(team[i].contents[0])
            score_dct = {'team':team_lst, 'score':score_lst}

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

    # Turn relative url to absolute using prefix
    def absoluteUrl(prefix, relative):
        '''
        Joins prefix with relative. Returns an absolute url.
        '''
        if prefix.endswith('/'):
            return prefix[:-1] + relative
        else:
            return prefix + relative
