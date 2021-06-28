import urllib
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
''' This code will crawl web to create features for ml model
    Import the above mentioned libraries and then run the class called FeatureCreation
    Class FeatureCreation creates features using different features and extract those features value to
    store it in a list called features
'''
class FeatureCreation:
    def __init__(self):
        # self.url = url
        ''' q stand for query here which will the name of company, we store 
        that query in self.c_name to be used in where ever company name is required
        '''
        q =[]
        q = 'abbott'
        self.c_name = q 
    
    def getURLForQuery(self):
        ''' This function crawls web to fetch the url, title, meta contents 
            It uses selenium web crawler, incase it does not work please inspect if containers mentioned find_element_by_xpath might have changed
            title will store the title contents
            link will store the link contents  
            detail will store the meta contents
            driver.close() will close selenium web crawler
        '''
        q = self.c_name 
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/search?q='+q)

        title = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//h3').text
        link = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//div[@class ="yuRUbf"]/a').get_attribute('href')
        detail = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]')
        self.title = title
        self.url = link
        self.meta = detail.text
        driver.close()
        return[self.title, self.url, self.meta]
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
    
    def appeared_in_title(self):
        '''This function counts the number of times company name has appeared in title tag of url
            we store title retrieved from web in string and query in substring
            then make both lower to count appeareance
        '''
        string = self.title
        substring = self.c_name
        count = string.lower().count(substring.lower())
        self.count = count
        return self.count 
    
    def appeared_in_meta(self):
        '''This function counts the number of times company name has appeared in meta tag of url
        '''
        string1 = self.meta
        substring1 = self.c_name
        count1 = string1.lower().count(substring1.lower())
        self.count1 = count1
        return self.count1
    
    def title_normalized(self):
        ''' This function divides the appeared in title value to no. of words in company name.
            we split the company name to count the number of words in it and then 
            divide that number to title appeared
        '''
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace 

        number_of_words = len(word_list)
        Count = self.count
        TN = Count/number_of_words
        return TN
    
    def meta_normalized(self):
        ''' This function divides the appeared in meta value to no. of words in company name.
            we split the company name to count the number of words in it and then 
            divide that number to meta appeared
        '''
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace

        number_of_words = len(word_list)
        #Count = appeared_in_meta(count1)
        Count = self.count1
        MN = Count/number_of_words
        return MN
    
    def lvtn(self):
        ''' To obtain the levenshtein distance between title and query submitted 
            it uses enchant library
        '''
        # s1 = getURLForQuery(title)
        s1 = self.title
        s2 = self.c_name
        # the Levenshtein distance between
        # string1 and string2
        return enchant.utils.levenshtein(s1, s2)
    
    def lvdn(self):
        ''' To obtain the levenshtein distance between domain and query submitted 
            it uses enchant library
        '''
        #s11 = getURLForQuery(url)
        s11 = self.url
        s22 = self.c_name
        # the Levenshtein distance between
        # string1 and string2
        return enchant.utils.levenshtein(s11, s22)
    
    def no_of_links(self):
        ''' To obtain links present in url and sum them to get total
        '''
        session = HTMLSession()
        r = session.get(self.url) # "http://www.abbott.com"
        unique_netlocs = Counter(urlparse(link).netloc for link in r.html.absolute_links)
        summ = 0
        for link in unique_netlocs:
            summ += unique_netlocs[link]#print(link, unique_netlocs[link])
            self.summ = summ
        return self.summ
    
    def word_count(self):
        ''' To obtain the total word count in html of a link
        '''
        url = self.url   #"https://aig.com"
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
        self.no_of_words = no_of_words
        return self.no_of_words
    
    def ratio_word_link(self):
        ''' function takes the ration of words obtained to links
        '''
        x = self.no_of_words
        y = self.summ # self.summ
        c = x/y
        return c 
    
    def cname_in_html(self):
        ''' This function checks if query appeared in tiltle, appeared in meta 
            if yes then it marks as 1
            if no then marks it as 0
        '''
        a = self.count # float(input("appeared in title "))
        b = self.count1 #float(input("appeared in meta: "))
        if(a <=0 and b <=0):
            return 0
        else:
            return 1    
    
    def feature_extract(self):
        ''' To call all above functions and store values obtained through them
            in a list called v which is further assigned to function
        '''
        geturl = self.getURLForQuery()
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
        ROP =1
        v = [ROP, Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL]
        self.v = v
        return self.v
peag = FeatureCreation()
features  = peag.feature_extract()