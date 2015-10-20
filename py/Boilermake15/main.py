from flask import Flask, url_for, render_template
from scripter import Scripter

app = Flask(__name__)

scripter = Scripter()

@app.route('/')
def redirect():
    front_page()

@app.route('/front')
def front_page():    
    return render_template('front.html', titles=scripter.SDtitles, links=scripter.SDlinks, 
                           githubHTML=scripter.GithubHTML, githubCSS=scripter.GithubCSS)

if __name__ == '__main__':
    app.run()