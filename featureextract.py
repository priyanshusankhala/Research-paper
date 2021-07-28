from getlinks import CrawlLinks

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
from urllib.parse import urlparse, urljoin
import pandas as pdclass


class FeatureCreation:
    def __init__(self):
        q = 'abbott'
        self.c_name = q 

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
            else:
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

    def ratio_we(self, external):
        no_of_words = self.no_of_words
        c=[x / y if y else 0 for x, y in zip(no_of_words, external)]  
        #print(str(c)) # Test
        return c 
    

    def ratio_et(self,external):
        summ = self.summ
        c=[x / y if y else 0 for x, y in zip(external, summ)]  
        #print(str(c)) # Test
        return c 
    
    
    def feature_extract(self):
        arr= []
        title = self.appeared_in_title()
        tn = self.title_normalized()
        meta = self.appeared_in_meta()
        mn = self.meta_normalized()
        lvtn = self.lvtn()
        lvdn = self.lvdn()
        links = self.no_of_links()
        word = self.word_count()
        dcnaih = self.cname_in_html()
        ratiowl = self.ratio_word_link()
        rop = self.rank_of_page()

        crawl_link = CrawlLinks(self.url)

        ext,int = crawl_link.ext_links()

        we = self.ratio_we(ext)
        et = self.ratio_et(ext)

        #v = [ROP, Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL]
        #mapped = zip(ROP, Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL)
        #mapped = set(mapped)
        #print(mapped)

        for v in zip(rop, title, tn, meta, mn, lvtn, lvdn, links, word, dcnaih, ratiowl,ext,int,we,et):
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
        print(self.v)
        return self.v