#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Authr  :hai~
Time    :2019/4/17 22:00
File    :123.py
"""
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


from app import views

