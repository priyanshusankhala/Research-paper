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
import pandas as pdclass FeatureCreation:

global total_urls_visited
global internal_urls
global external_urls

class FeatureCreation:
    def __init__(self):
        # self.url = url
        # ''' q stand for query here which will the name of company, we store 
        # that query in self.c_name to be used in where ever company name is required
        # '''
        q = 'abbott'
        self.c_name = company_name

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
    driver.get('https://www.google.com/search?q='+q+'%20WEBSITE&num=4') #+'%20WEBSITE&num=4' site:
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
    #print(self.url)
    return[self.meta,self.url, self.title]

    def is_valid(url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_all_website_links(self,url):
        urls = set()
        domain_name = urlparse(url).netloc
        soup = BeautifulSoup(requests.get(url, timeout =1).content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
            # href empty tag
                continue
            # join the URL if it's relative (not absolute link)
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid(href):
                continue
            if href in internal_urls:
                # already in the set
                continue
            if domain_name not in href:
                if href not in external_urls:
        #           print(f"{GRAY}[!] External link: {href}{RESET}")
                    external_urls.add(href)
                continue
        

        #print(f"{GREEN}[*] Internal link: {href}{RESET}")
            urls.add(href)
            internal_urls.add(href)
        return urls


def crawl(self, url, max_urls = 6):

    total_urls_visited += 1

    #print(f"{YELLOW}[*] Crawling: {url}{RESET}")
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)