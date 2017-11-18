#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:24:07 2017

@author: cheeyau
"""

from __future__ import print_function
from flask import Flask,request
from flask_cors import CORS,cross_origin
from PIL import Image
import sys

import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app,resources={r"/*": {"origins": "*"}},allow_headers='*')

print("initiated the app! With a name of:", __name__)

@app.route('/')
def index():

    print('Hello world!', file=sys.stderr)
    print('This standard output', file=sys.stdout)
    app.logger.info('Test')
    return "Hello, World!"

app = Flask(__name__)


@app.route("/img", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def home():
    content = request.get_json()
    #img = Image.open(request.files['file'])
    print(content,sys.stdout)
    sys.stdout.flush()
    #img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    return str(content)

    
if __name__ == '__main__':
    app.run(debug = True)