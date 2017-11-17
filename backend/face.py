#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:24:07 2017

@author: cheeyau
"""

from flask import Flask,request
from PIL import Image
import sys
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

app = Flask(__name__)

@app.route("/img", methods=["POST"])
def home():
    content = request.get_json()
    #img = Image.open(request.files['file'])
    print(content,sys.stdout)
    sys.stdout.flush()
    #img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    return str(content)
    
if __name__ == '__main__':
    app.run(debug = True)