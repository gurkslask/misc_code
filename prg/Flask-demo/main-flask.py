#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'alexander'

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/bild')
def bild():
    return render_template('bild.html')

if __name__ == '__main__':
    app.run(debug=True)