###### This code is adapted from stackoverflow ######
## TO FETCH TITLE TAG from a url
import requests
import lxml.html

response = requests.get('http://www.tcs.com')
tree = lxml.html.fromstring(response.text)
title_elem = tree.xpath('//title')[0]
title_elem = tree.cssselect('title')[0]  # equivalent to previous XPath
print("title tag:", title_elem.tag)
print("title text:", title_elem.text_content())
print("title html:", lxml.html.tostring(title_elem))
print("title tag:", title_elem.tag)
print("title's parent's tag:", title_elem.getparent().tag)







# outputs <Title>: IT Consulting Services & Business Solutions | Tata Consultancy Services (TCS)
############## TO FIND Number of links in a webpage

from requests_html import HTMLSession
from collections import Counter
from urllib.parse import urlparse

session = HTMLSession()
r = session.get("https://www.abbot.com")
unique_netlocs = Counter(urlparse(link).netloc for link in r.html.absolute_links)
for link in unique_netlocs:
    print(link, unique_netlocs[link])



# output 
# www.abbot.com 21
# printshopco.com 3
# www.facebook.com 1
# www.instagram.com 1
# www.shopify.com 1
# Abbot.com 1









################################################
### program to get the source code

import requests
import lxml
import cssselect

response = requests.get('http://www.tcs.com')
print(response.text)
import requests









###### To get the length of above source code 
## """ After placing the source code in between this we get length of it"""
from bs4 import BeautifulSoup
html_doc = """ """
soup = BeautifulSoup(html_doc, 'html.parser')
print("Length of the text of the first <html> tag:")
print(len(soup.find('html').text))




######## To check if the title is present in a given string of meta, title tag
import re
text = '3M Health Care · Science is our pursuit. · Healthcare markets · Get inspired by stories of innovation · Why warmth matters before, during and after surgery · How 3M ...‎Medical · ‎Health Information Systems · ‎Customer Service Excellence · ‎Oral Care'


for m in re.finditer('3M Health Care', text.lower()):
    print('3M Health Care', m.start(), m.end())


