#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Authr  :hai~
Time    :2019/4/17 23:28
File    :views.py
"""
from flask import render_template
from app import app

if __name__ == "__main__":
    app.run(host=app.config["HOST"], debug=app.config["DEBUG"], port=app.config["PORT"])

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    tofor = ['12','21','32']
    return render_template("index.html",
        title = 'Home',
        tofor = tofor,
        user = user)
@app.route('/<name>')
def name(name):
    return name