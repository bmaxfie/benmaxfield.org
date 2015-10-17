'''
Created on Oct 17, 2015

@author: Ben Maxfield
'''

from apscheduler.schedulers.background import BackgroundScheduler
from lxml import html
import requests

class Scripter():
    
    scheduler = None
    SDtitles = None


    def __init__(self):
        self.update()
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(self.update, 'interval', hours=1)
        
    def update(self):
        page = requests.get('http://feeds.sciencedaily.com/sciencedaily/top_news/top_technology?format=xml')
        tree = html.fromstring(page.text)
        self.SDtitles = tree.xpath('//item/title/text()')
        
