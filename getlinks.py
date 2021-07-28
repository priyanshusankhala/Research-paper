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

global total_urls_visited
global internal_urls
global external_urls

class CrawlLinks:
    def __init__(self,url):
        self.url = url
        pass

    def is_valid(url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_all_website_links(url):
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

    def crawl(url, max_urls=6):
        global total_urls_visited
        total_urls_visited += 1
        #print(f"{YELLOW}[*] Crawling: {url}{RESET}")
        links = get_all_website_links(url)
        for link in links:
            if total_urls_visited > max_urls:
                break
            crawl(link, max_urls=max_urls)

    def ext_links(self):
        # initialize the set of links (unique links)
        internal_urls = set()
        external_urls = set() 
        arr1 = []
        arr2 = []
        arr3 = []
        for i in self.url:
            try:
                self.crawl(i)
                arr1.append(len(external_urls))
                arr2.append(len(internal_urls))
                arr3.append(len(external_urls) + len(internal_urls))
                internal_urls = set()
                external_urls = set()
            except:
                #array.append([0,0,0])
                arr1.append(0)
                arr2.append(0)
                arr3.append(0)
                internal_urls = set()
                external_urls = set()
        # arr1 = list(filter('[]', arr1))
        # arr2 = list(filter('[]', arr2))
        # arr3 = list(filter([], arr3))
        #print(arr1,arr2)
        self.external = arr1
        self.internal = arr2
        
        return self.external,self.internal