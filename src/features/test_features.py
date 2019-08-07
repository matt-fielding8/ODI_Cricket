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
all_links = g.yearPageLinks(soup1)

years = ["2013", "2014", "2015", "2016","2017","2018","2019"]
filt_links = g.filterLinks(all_links, years)
abs_links = g.absoluteUrl("http://stats.espncricinfo.com/", filt_links)

match_ids = ['ODI # 3337', 'ODI # 3339', 'ODI # 3340', 'ODI # 3341',
       'ODI # 3342', 'ODI # 3353', 'ODI # 3354', 'ODI # 3355',
       'ODI # 3356', 'ODI # 3357', 'ODI # 3358', 'ODI # 3359',
       'ODI # 3395', 'ODI # 3397', 'ODI # 3399', 'ODI # 3402',
       'ODI # 3403', 'ODI # 3404', 'ODI # 3406', 'ODI # 3408',
       'ODI # 3409', 'ODI # 3410', 'ODI # 3417', 'ODI # 3418',
       'ODI # 3472', 'ODI # 3487', 'ODI # 3488', 'ODI # 3490',
       'ODI # 3491', 'ODI # 3503', 'ODI # 3504', 'ODI # 3505',
       'ODI # 3506', 'ODI # 3507', 'ODI # 3508', 'ODI # 3510',
       'ODI # 3513', 'ODI # 3518', 'ODI # 3521', 'ODI # 3524',
       'ODI # 3550', 'ODI # 3552', 'ODI # 3553', 'ODI # 3555',
       'ODI # 3556', 'ODI # 3558', 'ODI # 3559', 'ODI # 3560',
       'ODI # 3562', 'ODI # 3572', 'ODI # 3573', 'ODI # 3576',
       'ODI # 3581', 'ODI # 3601', 'ODI # 3603', 'ODI # 3604',
       'ODI # 3611', 'ODI # 3612', 'ODI # 3614', 'ODI # 3618',
       'ODI # 3620', 'ODI # 3621', 'ODI # 3622', 'ODI # 3624',
       'ODI # 3631', 'ODI # 3632', 'ODI # 3633', 'ODI # 3636',
       'ODI # 3637', 'ODI # 3638', 'ODI # 3639', 'ODI # 3650',
       'ODI # 3651', 'ODI # 3652', 'ODI # 3653', 'ODI # 3662',
       'ODI # 3665', 'ODI # 3667', 'ODI # 3673', 'ODI # 3674',
       'ODI # 3675', 'ODI # 3679', 'ODI # 3685', 'ODI # 3686',
       'ODI # 3687', 'ODI # 3693', 'ODI # 3694', 'ODI # 3696',
       'ODI # 3697', 'ODI # 3699', 'ODI # 3703', 'ODI # 3705',
       'ODI # 3706', 'ODI # 3713', 'ODI # 3716', 'ODI # 3719',
       'ODI # 3720', 'ODI # 3722', 'ODI # 3742', 'ODI # 3744',
       'ODI # 3746', 'ODI # 3748', 'ODI # 3749', 'ODI # 3759',
       'ODI # 3760', 'ODI # 3761', 'ODI # 3762', 'ODI # 3763',
       'ODI # 3764', 'ODI # 3767', 'ODI # 3780', 'ODI # 3782',
       'ODI # 3804', 'ODI # 3806', 'ODI # 3807', 'ODI # 3809',
       'ODI # 3810', 'ODI # 3835', 'ODI # 3837', 'ODI # 3838',
       'ODI # 3840', 'ODI # 3842', 'ODI # 3850', 'ODI # 3851',
       'ODI # 3852', 'ODI # 3853', 'ODI # 3854', 'ODI # 3864',
       'ODI # 3865', 'ODI # 3866', 'ODI # 3867', 'ODI # 3869',
       'ODI # 3870', 'ODI # 3897', 'ODI # 3899', 'ODI # 3901',
       'ODI # 3903', 'ODI # 3904', 'ODI # 3935', 'ODI # 3937',
       'ODI # 3940', 'ODI # 3952', 'ODI # 3955', 'ODI # 3962',
       'ODI # 3964', 'ODI # 3972', 'ODI # 3974', 'ODI # 3975',
       'ODI # 3977', 'ODI # 3979', 'ODI # 3983', 'ODI # 3987',
       'ODI # 3988', 'ODI # 3990', 'ODI # 3991', 'ODI # 3993',
       'ODI # 4002', 'ODI # 4003', 'ODI # 4004', 'ODI # 4006',
       'ODI # 4008', 'ODI # 4015', 'ODI # 4017', 'ODI # 4019',
       'ODI # 4020', 'ODI # 4021', 'ODI # 4032', 'ODI # 4033',
       'ODI # 4035', 'ODI # 4037', 'ODI # 4039', 'ODI # 4049',
       'ODI # 4050', 'ODI # 4051', 'ODI # 4057', 'ODI # 4060',
       'ODI # 4061', 'ODI # 4100', 'ODI # 4101', 'ODI # 4105',
       'ODI # 4108', 'ODI # 4110', 'ODI # 4127', 'ODI # 4128',
       'ODI # 4131', 'ODI # 4132', 'ODI # 4136', 'ODI # 4139']

missing_score_links = g.scorecardLinks(abs_links, match_ids)
abs_sc_links = g.absoluteUrl("https://www.espncricinfo.com/", missing_score_links)
print(len(match_ids), len(missing_score_links))
print(abs_sc_links)

assert len(match_ids)==len(missing_score_links)