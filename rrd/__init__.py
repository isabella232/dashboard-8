#-*- coding:utf-8 -*-
import os
from flask import Flask

#-- create app --
app = Flask(__name__)
app.config.from_object("rrd.config")

@app.errorhandler(Exception)
def all_exception_handler(error):
    print "exception: %s" %error
    return u'dashboard is down, contact administrator', 500

from view import api, chart, screen, index
