'''
Created on Oct 17, 2015

@author: Ben Maxfield
'''

from time import clock
from flask import Markup
from apscheduler.schedulers.background import BackgroundScheduler
from lxml import html, etree
import requests
import feedparser

class Scraper():
    
    scheduler = None
    script = '''
        > python scraper.py
        STARTING WEB SCRAPER...
        =========================|
        000%|====================|
        =========================|
        
        GETting first target:
        address=\"https://github.com/bmaxfie\"
        .
        .
        .
        RETRIEVED .html, {} KB
        PARSING .html
        FOUND commit stats!
        ADDED markup to front.html template
        FOUND .css links!
        ADDED markup to front.html template
        FOUND .js links!
        ADDED markup to front.html template
        ANIMATING...
        
        GETting second target:
        address=\"http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml\"
        .
        .
        .
        RETRIEVED .xml, {} KB
        PARSING .xml
        FOUND top 3 articles!
        ADDED markup to front.html template
        ANIMATING...
        
        =========================|
        WEB SCRAPER COMPLETE
        
        >
        '''
    SDtitles = ['', '', '']
    SDlinks = ['', '', '']
    SDtimestamp = 0
    GithubHTML = None
    GithubCSS = None


    def __init__(self):
        self.update()
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(self.update, 'interval', hours=1)
        
    def update(self):
        # Saves the top 3 article titles and links from ScienceDaily.com under the Technology category.
        feed = feedparser.parse('http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml')
        for i in range(0,3):
            self.SDtitles[i] = feed.entries[i].title
            self.SDlinks[i] = feed.entries[i].link
        self.SDtimestamp = clock()
        SDsize = feed.__sizeof__() * 100.0 / 1000 # SOMETHING IS WRONG HERE, This XML is not ~508 Bytes... its at least 5 KB.
        
        # Gets bmaxfie@Github public data and .css from page
        page = requests.get('https://github.com/bmaxfie')
        tree = html.fromstring(page.text)
        self.GithubHTML = Markup(etree.tostring(tree.xpath('//div[@class="boxed-group flush"]')[1], pretty_print=True))
        GithubSize = page.__sizeof__() * 1000.0 / 1000 # SOMETHING IS WRONG HERE, see above comment
        
        strings = ""
        for element in tree.xpath('//link[@rel="stylesheet"]'):
            strings = strings + etree.tostring(element, pretty_print=True)
        self.GithubCSS = Markup(strings)
        
        self.script = self.script.format(SDsize, GithubSize)
        print(self.script)
        
