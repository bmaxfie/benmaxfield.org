'''
Created on Oct 17, 2015

@author: Ben Maxfield
'''

import os
from time import clock
from flask import Flask, url_for, render_template, redirect, request
from scraper import Scraper

app = Flask(__name__)

#admin = Blueprint('admin', __name__, static_folder='res')
scripter = Scraper()


def getSDtimediff():
    secs = int((clock() - scripter.SDtimestamp) % 60)
    mins = int((clock() - scripter.SDtimestamp) / 60)
    return `mins` + " mins, " + `secs` + " secs"

@app.route('/')
def redirect_front_page():
    return redirect("/front", code=302)

@app.route('/front')
def front_page():
    return render_template('/front.html', titles=scripter.SDtitles, links=scripter.SDlinks, githubHTML=scripter.GithubHTML, githubCSS=scripter.GithubCSS, timediff=getSDtimediff())

# DEPRECATED PAGE:
@app.route('/Resume.html')
def resume_page():
    print(os.getcwd())
    return render_template('Resume.html')

if __name__ == '__main__':
    app.run()