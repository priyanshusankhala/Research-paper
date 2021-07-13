import urllib
import json as m_json
from urllib import request
from urllib.parse import urlparse
import sys
import enchant
from numpy import array
from requests_html import HTMLSession
from collections import Counter
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
from selenium import webdriver
import ssl
import requests

# ''' This code will crawl web to create features for ml model
#     Import the above mentioned libraries and then run the class called FeatureCreation
#     Class FeatureCreation creates features using different features and extract those features value to
#     store it in a list called features
# '''
class FeatureCreation:
    def __init__(self):
        # self.url = url
        # ''' q stand for query here which will the name of company, we store 
        # that query in self.c_name to be used in where ever company name is required
        # '''
        q =[]
        q = 'abbott'
        self.c_name = q 
    
    def getURLForQuery(self):
        # ''' This function crawls web to fetch the url, title, meta contents 
        #     It uses selenium web crawler, incase it does not work please inspect if containers mentioned find_element_by_xpath might have changed
        #     title will store the title contents
        #     link will store the link contents  
        #     detail will store the meta contents
        #     driver.close() will close selenium web crawler
        # '''
        # q = self.c_name 
        # driver = webdriver.Chrome()
        # driver.get('https://www.google.com/search?q='+q)

        # title = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//h3').text
        # link = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//div[@class ="yuRUbf"]/a').get_attribute('href')
        # detail = driver.find_element_by_xpath('//div[@class="g"]').find_element_by_xpath('.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]')
        # self.title = title
        # self.url = link
        # self.meta = detail.text
        # driver.close()
        # print(self.title, self.url)
        # return[self.title, self.url, self.meta]
        arr1 = []
        arr2 = []
        arr3 = []
        q =[]
        q = self.c_name 
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/search?q='+q+'%20WEBSITE&num=4') #+'%20WEBSITE&num=4'
        for element in driver.find_elements_by_xpath('//div[@class="g"]'):
            ##title = element.find_element_by_xpath('.//h3').find_element_by_xpath('.//h3[@class = "LC20lb DKV0Md"]').text
            title = element.find_element_by_xpath('.//h3[@class = "LC20lb DKV0Md"]').text
            link = element.find_element_by_xpath('.//div[@class ="yuRUbf"]/a').get_attribute('href')
            # link = element.find_element_by_xpath('.//div[@class ="yuRUbf"]').find_element_by_xpath('.//div[@class = "TbwUpd NJjxre"]').text
            ##.find_element_by_xpath('.//cite[@class = "iUh30 Zu0yb qLRx3b tjvcx"]')
            ##detail = element.find_element_by_xpath('.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]').text
            detail = element.find_element_by_xpath('.//div[@class="IsZvec"]').text
            #print(detail)
            #print(link)
            # print(title)
            arr1.append(title)
            arr2.append(link)
            arr3.append(detail)
        arr2 = list(filter(None, arr2))
        arr1 = list(filter(None, arr1))
        arr3 = list(filter(None, arr3))
        self.title = arr1
        self.url = arr2
        self.meta = arr3
        #print(arr1, arr2, arr3) # Test
        #return self.title    
        return[self.meta,self.url, self.title]
        # driver.close()
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
        # '''This function counts the number of times company name has appeared in title tag of url
        #     we store title retrieved from web in string and query in substring
        #     then make both lower to count appeareance
        # '''
        arr = []
        string = self.title
        substring = self.c_name
        for i in string:
            res = i.lower().count(substring.lower())
            arr.append(res)
        #self.count
        self.count = arr
        #print(self.count) # Test
        return self.count 
    
    def appeared_in_meta(self):
        # '''This function counts the number of times company name has appeared in meta tag of url
        # '''
        arr = []
        string1 = self.meta
        substring1 = self.c_name
        for i in string1:
            res1 = i.lower().count(substring1.lower())
            arr.append(res1)
        self.count1 = arr
        #print(self.count1) # Test
        return self.count1
    
    def title_normalized(self):
        arr = []
        # ''' This function divides the appeared in title value to no. of words in company name.
        #     we split the company name to count the number of words in it and then 
        #     divide that number to title appeared
        # '''
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace 

        number_of_words = len(word_list)
        for i in self.count:
            Count = i
            TN = Count/number_of_words
            arr.append(TN)
        #print(arr) #Test
        TN = arr
        return TN
    
    def meta_normalized(self):
        # ''' This function divides the appeared in meta value to no. of words in company name.
        #     we split the company name to count the number of words in it and then 
        #     divide that number to meta appeared
        # '''
        arr = []
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace

        number_of_words = len(word_list)
        #Count = appeared_in_meta(count1)
        for i in self.count1:
            Count = i
            MN = Count/number_of_words
            arr.append(MN)
        #print(arr) #Test
        MN = arr
        return MN
    
    def lvtn(self):
        arr = []
        for i in self.title:
            s1 = i
            s2 = self.c_name
            arr.append(enchant.utils.levenshtein(s1, s2))
        #print(arr) #Test
        return arr
    
    
    def lvdn(self):
        # ''' To obtain the levenshtein distance between domain and query submitted 
        #     it uses enchant library
        # '''
        #s11 = getURLForQuery(url)
        arr1 = []
        for i in self.url:
            s11 = i
            s22 = self.c_name
            arr1.append(enchant.utils.levenshtein(s11, s22))
        #print(arr1) # Test
        return arr1
    
    def no_of_links(self):
        arr = []
        session = HTMLSession()
        for i in self.url:
            try:
                r = session.get(i,verify=False) # "http://www.abbott.com"
                unique_netlocs = Counter(urlparse(link).netloc for link in r.html.absolute_links)
                summ = 0
                for link in unique_netlocs:
                    try:
                        summ += unique_netlocs[link]#print(link, unique_netlocs[link]
                    except Exception as e:
                        summ =0            
                arr.append(summ)
            except requests.exceptions.ProxyError:
                arr.append(0)
        self.summ = arr
        #print(self.summ) #Test
        return self.summ
        #print(arr)


    def word_count(self):
        # ''' To obtain the total word count in html of a link
        # '''
        arr = []
        for i in self.url:
            url = i   #"https://aig.com"
            context = ssl._create_unverified_context()
            #urllib.urlopen("https://no-valid-cert", context=context)
            try:
                html = urlopen(url, context=context)

                soup = BeautifulSoup(html, "html.parser")
                type(soup)

                all_links = soup.findAll('html')
                str_cells = str(all_links)
                cleartext = BeautifulSoup(str_cells, "html.parser").get_text()

                #print(cleartext)
                a_string = cleartext

                word_list = a_string.split()
                no_of_words = len(word_list)
                arr.append(no_of_words)
            except urllib.error.HTTPError as e:
                #print('0')
                arr.append(0)
        self.no_of_words = arr
        #print(self.no_of_words)#Test
        return self.no_of_words
        #print(arr)
        #return self.no_of_words
    
    def ratio_word_link(self):
        no_of_words = self.no_of_words
        summ = self.summ
        c=[x / y if y else 0 for x, y in zip(no_of_words, summ)]  
        #print(str(c)) # Test
        return c 
    
    def cname_in_html(self):
        arr =[]
        l1 = self.count # float(input("appeared in title "))
        l2 = self.count1 #float(input("appeared in meta: "))
        for x, y in zip(l1, l2):
            if x<=0 and y<=0:
                #print(0)
                v = 0
            #return False
            else:
                #print(1)
                v = 1
            arr.append(v)
        #print(arr) #Test
        return arr
    def rank_of_page(self):
        names = self.url
        numbers = []
        num =1
        for item in range(len(names)):
            if item == len(names) - 1:
                break
            elif names[item] == names[item+1]:
                numbers.append(num)
            else:
                numbers.append(num)
                num = num + 1
        numbers.append(num)
        return numbers
        #print(numbers) # Test
    
    def feature_extract(self):
        arr= []
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
        ROP = self.rank_of_page()
        #v = [ROP, Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL]
        #mapped = zip(ROP, Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL)
        #mapped = set(mapped)
        #print(mapped)
        for v in zip(ROP, Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL):
            # print([v])
            #res =  [ v[i] for i in () ]
            #res = v[::] 
            #print(str(res))
            #mat1 = np.array(v)
            #print(mat1)
            #print(mat1[[0]])
        #print(v)
            arr.append(v)
        self.v = arr
        return self.v
    
    def get_url(self):
        #geturl = self.getURLForQuery()
        z = self.url
        #print(z)
        return z
        #return geturl[1]
peag = FeatureCreation()
features  = peag.feature_extract()
displayurl = peag.get_url()