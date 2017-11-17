#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:24:07 2017

@author: cheeyau
"""

from flask import Flask,request
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route("/img", methods=["POST"])
def home():
    img = Image.open(request.files['file'])
    img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    return 'Success!'
    
if __name__ == '__main__':
    app.run(debug = True)