import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

def getSoup(url):
    '''
    Returns soup for url response object.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

print(getSoup("http://stats.espncricinfo.com/ci/content/records/307851.html"))




