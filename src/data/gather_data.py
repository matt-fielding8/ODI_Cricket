"""
All the scripts required to gather missing data from
https://www.espncricinfo.com/
"""
from bs4 import BeautifulSoup
import requests

class Gather:
    def __init__(self):
        pass

    def getSoup(self, url):
        '''
        Returns soup for url response object.
        '''
        r = requests.get(url)
        self.soup = BeautifulSoup(r.content, "html.parser")
        return self.soup

    # Gather missing score data
    def getMissingData(self, url):
        ''' str -> dct
        Uses requests and bs4 libraries to extract and parse html data from url.
        Returns a dct with 'team' and 'score' indices.
        '''
        soup = self.getSoup(url)
        # Extract match_id
        match_id = soup.find(lambda tag: tag.name == 'a' and 'ODI no' in tag.get_text()).contents
        # Extract score data from soup
        score = soup.find_all(class_='cscore_score')
        score_lst = [i.contents[0] for i in score]
        # Extract team data from soup
        team = soup.find_all(class_='cscore_name--long')
        team_lst =  [i.contents[0] for i in team]
        # Extract detailed score data from soup
        ## Find tags containg "TOTAL"
        tot_tags = soup.find_all(lambda tag: tag.name == 'div' and \
            tag.get('class')==['cell'] and tag.get_text()=='TOTAL')
        detailed_score = [i.findNext().contents[0] for i in tot_tags]
        # Write information to dct
        score_dct = {'match_id':match_id*2,
                    'team':team_lst[:2],
                    'score':score_lst[:2],
                    'detailed_score':detailed_score}

        return score_dct

    # Get page links directing to all results per year
    def yearPageLinks(self, soup):
        ''' wb -> list of str
        Extracts relative links in "QuoteSummary" class from soup.
        Returns relative url's as a list of str.
        '''
        self.link_list = []
        try:
            for i in soup.find_all(class_='QuoteSummary'):
                self.link_list.append(i['href'])
        except:
            print('Class "QuoteSummary" does not exist')

        return self.link_list

    # Filter links based on criteria
    def filterLinks(self, links, lst):
        """ (list of str, list of str) -> list of str
        Filters elements in links which contain elements in lst as a substring.
        Returns filtered elements as a list.
        """
        self.filt_links = ([(list(filter(lambda x: i in x, links))) for i in lst])
        # Flatten filt_links list
        return [i for link in self.filt_links for i in link]

    # Turn relative url to absolute using prefix
    def absoluteUrl(self, prefix, relative):
        '''
        Joins prefix with relative. Returns an absolute url.
        '''
        prefix = prefix.rstrip('/')
        return [prefix + link for link in relative]

    # Get scorecard links
    def scorecardLinks(self, year_links, match_ids):
        ''' (lst of str, list of str) -> list of str
        Loops through year_links and returns a list of relative links for all
        id's in match_ids.
        '''
        # Generate soup for all year_links
        soups = [self.getSoup(link) for link in year_links]
        # Retrieve all links within each soup
        raw_links = [soup.find_all(['tr', 'td','a'], class_=['data-link'], attrs=['href']) for soup in soups]

        # Extract all links associated with elements in match_ids
        sc_links_found = []
        for year_page in raw_links:
            for link in year_page:
                if link.contents[0] in match_ids:
                    sc_links_found.append(link['href'])

        return sc_links_found
