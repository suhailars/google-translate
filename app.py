import os
from flask import Flask, render_template, request, json, url_for, redirect
import urllib
from api import translate

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translator():
    word =  str(request.form['english'])
    lang = str(request.form['lang'])
    resp = translate('en', lang, word)
    return json.dumps({'status':'OK', 'resp':resp})

if __name__=="__main__":
    app.run(debug=True)
