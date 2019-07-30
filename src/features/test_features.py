# from bs4 import BeautifulSoup
# import requests
#
# url = "http://stats.espncricinfo.com/ci/content/records/307851.html"
#
# def getSoup(url):
#     '''
#     Returns soup for url response object.
#     '''
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, "html.parser")
#     return soup
#
# # print(getSoup(url))
#
# def yearPageLinks(soup):
#     ''' wb -> list of str
#     Extracts relative links in "QuoteSummary" class from soup.
#     Returns relative url's as a list of str.
#     '''
#     link_list = []
#     try:
#         for i in soup.find_all(class_='QuoteSummary'):
#             link_list.append(i['href'])
#     except:
#         print('Class "QuoteSummary" does not exist')
#
#     return link_list
#
# print(yearPageLinks(getSoup(url)))
#
# prefix = "http://stats.espncricinfo.com/"
# rel = "/ci/engine/records/team/match_results.html?class=2;id=1971;type=year"
#
# def absoluteUrl(prefix, relative):
#     '''
#     Joins prefix with relative. Returns an absolute url.
#     '''
#     if prefix.endswith('/'):
#         return prefix[:-1] + relative
#     else:
#         return prefix + relative
#
# print(absoluteUrl(prefix, rel))

from src.data.gather_data import Gather

url = "http://stats.espncricinfo.com/ci/content/records/307851.html"

g = Gather()
soup1 = g.getSoup(url)
links = g.yearPageLinks(soup1)
print(links)
abs_links = g.absoluteUrl("http://stats.espncricinfo.com/", links)
print(abs_links)
abs_links2 = g.absoluteUrl("http://stats.espncricinfo.com////////", links)
print(abs_links == abs_links2)

years = ["2013", "1024", "2015", "2016","2017","2018","2019"]

filt_list1 = g.filterLinks(links, years)
filt_list2 = g.filterLinks(abs_links, years)
print(filt_list1)
print(filt_list2)