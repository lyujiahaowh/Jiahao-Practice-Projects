'''
What is Web Scraping?
- When a program or script pretends to be a browser and retrieves web pages, 
looks at those web pages, extracts information, and then looks at more web pages
- Search engines scrape web pages - we call this "spidering the web" or "web crawling"

Why Scrape?
- Pull data - particularly social data - who links to who?
- Get your own data back out of some system that has no "export capability"
- Monitor a site for new information
- Spider the web to make a database for search engine

Scraping Web Pages
- There is some controversy about web page scraping and some sites are a bit snippy about it
- Republishing copyrighted information is not allowed
- Violating terms of service is not allowed 

The Easy Way - Beautiful Soup
- You could do string searches the hard way
- Or use the free software library called BeautifulSoupfrom www.crummy.com

BeautifulSoup Installation
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4,zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

e.g. code
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautfulSoup(html, 'html.parser')

# Retrieve all of the anchor tag 
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    
Summary
- The TCP/IP gives us pipes / sockets between applications
- We designed application protocols to make use of these pipes
- HyperText Transfer Protocol(HTTP) is a simple yet powerfull protocol
- Python has good support for sockets, HTTP, and HTML parsing
'''