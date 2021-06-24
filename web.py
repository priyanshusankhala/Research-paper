#import urllib3
import json as m_json
from urllib.parse import urlparse
import sys
import enchant
from requests_html import HTMLSession
from collections import Counter
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

def getURLForQuery(q):
    # q =[]
    # q = 'abbott' 
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q='+q)

    titl = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//h3')
    link = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//div[@class ="yuRUbf"]/a').get_attribute('href')
    detail = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]')
    driver.close()
    title = titl.text
    url = link
    meta = detail.text
    return[title.text, url, meta.text]
# def getURLForQuery(q):
#     URLS = []
#     for result in q:
#         title = result['title']
#         meta = result['meta']
#         url = result['url']   # was URL in the original and that threw a name error exception
#         URLS.append(url)
#         return title
#         return meta
#         return url
# def getURLForQuery(q, query2URLS):
#   #  query = urllib3.urlencode ( { 'q' : q } )
#    # response = urllib3.urlopen ( 'http://googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
#    # json = m_json.loads ( response )
#     results = json [ 'responseData' ] [ 'results' ]
#     URLS = []
#     for result in results:
#         title = result['title']
#         meta = result['meta']
#         url = result['url']   # was URL in the original and that threw a name error exception
#         URLS.append(url)
#         return title
#         return meta
#         return url
#     query2URLS[q] = URLS




# def getRankedURLSLst(urls):
#     # store the rank of each url
#     rankedURLSDict = {}
#     min_url_rank = sys.maxint
#     max_url_rank = -sys.maxint
#     for i, url in enumerate(urls):
#         return sorted([(k, float(rankedURLSDict[k] - min_url_rank)


class FeatureCreation:
    def __init__(self, url,c_name):
        self.url = url
        self.c_name = c_name
    def appeared_in_title(self):
        string = getURLForQuery(title)
        substring = self.c_name
        count = string.lower().count(substring.lower())
        return count
    def appeared_in_meta(self):
        string1 = getURLForQuery(meta)
        substring1 = self.c_name
        count1 = string1.lower().count(substring1.lower())
        return count1
    def title_normalized(self):
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace

        number_of_words = len(word_list)
        Count = appeared_in_title(count)
        TN = Count/number_of_words
        return TN
    def meta_normalized(self):
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace

        number_of_words = len(word_list)
        Count = appeared_in_meta(count1)
        MN = Count/number_of_words
        return MN
    def lvtn(self):
        s1 = getURLForQuery(title)
        s2 = self.c_name
        # the Levenshtein distance between
        # string1 and string2
        print(enchant.utils.levenshtein(s1, s2))
    def lvdn(self):
        s11 = getURLForQuery(url)
        s22 = c_name
        # the Levenshtein distance between
        # string1 and string2
        print(enchant.utils.levenshtein(s11, s22))
    def no_of_links(self):
        session = HTMLSession()
        r = session.get(getURLForQuery(url)) # "http://www.abbott.com"
        unique_netlocs = Counter(urlparse(link).netloc for link in r.html.absolute_links)
        summ = 0
        for link in unique_netlocs:
            summ += unique_netlocs[link]#print(link, unique_netlocs[link])
        return summ
    def word_count(self):
        
        url = getURLForQuery(url)   #"https://aig.com"
        html = urlopen(url)

        soup = BeautifulSoup(html, "html.parser")
        type(soup)

        all_links = soup.findAll('html')
        str_cells = str(all_links)
        cleartext = BeautifulSoup(str_cells, "html.parser").get_text()

        #print(cleartext)
        a_string = cleartext

        word_list = a_string.split()
        no_of_words = len(word_list)

        return no_of_words
    def ratio_word_link(self):
        x = word_count(no_of_words)
        y = no_of_links(links)
        c = x/y
        return c 
    def cname_in_html(self):
        a = appeared_in_title(count) # float(input("appeared in title "))
        b = appeared_in_meta(count1) #float(input("appeared in meta: "))
        if(a <=0 and b <=0):
            return 0
        else:
            return 1    
    def feature_extract(self):
        Title = self.appeared_in_title()
        TN = self.title_normalized()
        Meta = self.appeared_in_meta()
        MN = self.meta_normalized()
        LVTN = self.lvtn()
        LVDN = self.lvdn()
        Links = self.no_of_links()
        Word = self.word_count()
        DCNAIH = self.cname_in_html()
        RatioWL = self.ratio_word_link()
        v = [Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL]
        return v
