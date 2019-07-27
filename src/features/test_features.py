import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

url = "http://stats.espncricinfo.com/ci/content/records/307851.html"

def getSoup(url):
    '''
    Returns soup for url response object.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

# print(getSoup(url))

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

print(yearPageLinks(getSoup(url)))

