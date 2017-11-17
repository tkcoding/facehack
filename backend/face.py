#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:24:07 2017

@author: cheeyau
"""

from __future__ import print_function
from flask import Flask,request
from PIL import Image
import sys
<<<<<<< HEAD
import logging
from logging.handlers import RotatingFileHandler

=======
>>>>>>> 7f776adf54daeee5ca7ed1475dd07cd61097cdbc

app = Flask(__name__)
print("initiated the app! With a name of:", __name__)

@app.route('/')
def index():

    print('Hello world!', file=sys.stderr)
    print('This standard output', file=sys.stdout)
    app.logger.info('Test')
    return "Hello, World!"

app = Flask(__name__)
<<<<<<< HEAD

@app.route("/img", methods=["POST"])
def home():
    content = request.get_json()
    #img = Image.open(request.files['file'])
    print(content,sys.stdout)
    sys.stdout.flush()
    #img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    return str(content)
=======
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route("/img", methods=["POST"])
def home():
    print('Hello world!', file=sys.stderr)
    print('This standard output', file=sys.stdout)
    app.logger.info('Test')
    img = Image.open(request.files['file'])
    img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    return 'Success!'
>>>>>>> 7f776adf54daeee5ca7ed1475dd07cd61097cdbc
    
if __name__ == '__main__':
    app.run(debug = True)