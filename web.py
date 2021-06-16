import urllib3
import json as m_json
from urllib.parse import urlparse
import sys
import enchant

def getURLForQuery(q, query2URLS):
    query = urllib3.urlencode ( { 'q' : q } )
    response = urllib3.urlopen ( 'http://googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    URLS = []
    for result in results:
        title = result['title']
        meta = result['meta']
        url = result['url']   # was URL in the original and that threw a name error exception
        URLS.append(url)
    query2URLS[q] = URLS




def getRankedURLSLst(urls):
    # store the rank of each url
    rankedURLSDict = {}
    min_url_rank = sys.maxint
    max_url_rank = -sys.maxint
    for i, url in enumerate(urls):
        return sorted([(k, float(rankedURLSDict[k] - min_url_rank)


class feature_creation:
    
    def __init__(self, c_name):
        self.c_name = Company_name
    
    def appeared_in_title(self):
        string = title
        substring = self.c_name
        count = string.lower().count(substring.lower())
        return count
    def appeared_in_meta(self):
        string1 = meta
        substring1 = self.c_name
        count1 = string1.lower().count(substring1.lower())
        return count1
    def title_normalized(self):
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace

        number_of_words = len(word_list)
        Count = count
        TN = Count/number_of_words
        return TN
    def meta_normalized(self):
        a_string = self.c_name
        word_list = a_string.split()
        #Split `a_string` by whitespace

        number_of_words = len(word_list)
        Count = count1
        MN = Count/number_of_words
        return MN
    def LVTN(self):
        s1 = title
        s2 = c_name
        # the Levenshtein distance between
        # string1 and string2
        print(enchant.utils.levenshtein(s1, s2))
    def LVDN(self):
        s11 = url
        s22 = c_name
        # the Levenshtein distance between
        # string1 and string2
        print(enchant.utils.levenshtein(s11, s22))
    def no_of_links(self):
        from requests_html import HTMLSession
        from collections import Counter
        from urllib.parse import urlparse

        session = HTMLSession()
        r = session.get(url) # "http://www.abbott.com"
        unique_netlocs = Counter(urlparse(link).netloc for link in r.html.absolute_links)
        summ = 0
        for link in unique_netlocs:
        summ += unique_netlocs[link]
        #print(link, unique_netlocs[link])
        print(summ)
    def word_count(self):
        from bs4 import BeautifulSoup
        from urllib.request import urlopen

        url = url   #"https://aig.com"
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

        print(no_of_words)
    def ratio_word_link(self):
        x = no_of_words
        y = links
        c = x/y
        return c 
    def Does_CName_Appear_In_Html(self):
        a = count # float(input("appeared in title "))
        b = count1 #float(input("appeared in meta: "))
        if(a > 0 and b > 0) :
            print("1".format(a, b))
        elif(a <= 0 and b > 0):
            print("1".format(b, a))
        elif(a > 0 and b <= 0):
            print("1".format(b, a))
        else:
            print("0")    
    def feature_extract(self):
        Title = self.appeared_in_title()
        TN = self.title_normalized()
        Meta = self.appeared_in_meta()
        LVTN = self.LVTN()
        LVDN = self.LVDN()
        Links = self.no_of_links()
        Word = self.word_count()
        DCNAIH = self.Does_CName_Appear_In_Html()
        RatioWL = self.ratio_word_link()
        v = [Title, TN, Meta, MN, LVTN, LVDN, Links, Word, DCNAIH, RatioWL]
        
