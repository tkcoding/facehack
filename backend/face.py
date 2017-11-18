#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 01:24:07 2017

@author: cheeyau
"""

from __future__ import print_function
from flask import Flask,request,Response
from flask_cors import CORS,cross_origin
from PIL import Image
import sys
import numpy as np
import logging
from logging.handlers import RotatingFileHandler
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app,resources={r"/*": {"origins": "*"}},allow_headers='*')

print("initiated the app! With a name of:", __name__)

def process_json(content):

    feature_dictionary = {}
    json_result = json.loads(content)
    analysis = []

    feature_dictionary['eyebrowLeft2'] = json_result['objects'][1]['landmarks']['eyebrowLeft'][2]
    feature_dictionary['eyebrowRight2'] = json_result['objects'][1]['landmarks']['eyebrowRight'][2]
    feature_dictionary['eyeLeftAvg'] = np.divide(np.sum([json_result['objects'][1]['landmarks']['eyeLeft'][1],json_result['objects'][1]['landmarks']['eyeLeft'][2]],axis=0),2)
    feature_dictionary['eyeRightAvg'] = np.divide(np.sum([json_result['objects'][1]['landmarks']['eyeRight'][1],json_result['objects'][1]['landmarks']['eyeRight'][2]],axis=0),2)
    feature_dictionary['eyeRight3'] = json_result['objects'][1]['landmarks']['eyeRight'][3]
    feature_dictionary['eyeRight0'] = json_result['objects'][1]['landmarks']['eyeRight'][0]
    feature_dictionary['eyeLeft3'] = json_result['objects'][1]['landmarks']['eyeLeft'][3]
    feature_dictionary['eyeLeft0'] = json_result['objects'][1]['landmarks']['eyeLeft'][0]
    feature_dictionary['eyeLeftC'] = np.divide(np.sum([json_result['objects'][1]['landmarks']['eyeLeft'][4],json_result['objects'][1]['landmarks']['eyeLeft'][5]],axis=0),2)
    feature_dictionary['eyeRightC'] = np.divide(np.sum([json_result['objects'][1]['landmarks']['eyeRight'][4],json_result['objects'][1]['landmarks']['eyeRight'][5]],axis=0),2)
    feature_dictionary['faceContour2'] = json_result['objects'][1]['landmarks']['faceContour'][2]
    feature_dictionary['noseBall0'] = json_result['objects'][1]['landmarks']['noseBall'][0]
    feature_dictionary['noseBall2'] = json_result['objects'][1]['landmarks']['noseBall'][2]
    feature_dictionary['noseBall4'] = json_result['objects'][1]['landmarks']['noseBall'][4]
    feature_dictionary['faceContour14'] = json_result['objects'][1]['landmarks']['faceContour'][14]
    feature_dictionary['mouthOuter2'] = json_result['objects'][1]['landmarks']['mouthOuter'][2]
    feature_dictionary['mouthOuter3'] = json_result['objects'][1]['landmarks']['mouthOuter'][3]
    feature_dictionary['mouthOuter4'] = json_result['objects'][1]['landmarks']['mouthOuter'][4]
    feature_dictionary['mouthOuter0'] = json_result['objects'][1]['landmarks']['mouthOuter'][0]
    feature_dictionary['mouthInnerAvg'] = np.divide(np.sum([json_result['objects'][1]['landmarks']['mouthInner'][2],json_result['objects'][1]['landmarks']['mouthInner'][6]],axis=0),2)
    feature_dictionary['mouthOuter6'] = json_result['objects'][1]['landmarks']['mouthOuter'][6]
    feature_dictionary['mouthOuter9'] = json_result['objects'][1]['landmarks']['mouthOuter'][9]
    feature_dictionary['faceContour8'] = json_result['objects'][1]['landmarks']['faceContour'][8]

    canon_5 = abs(np.divide(float(np.subtract(feature_dictionary['eyeRight0'][0],feature_dictionary['eyeLeft3'][0])),float(np.subtract(feature_dictionary['noseBall4'][0],feature_dictionary['noseBall0'][0]))))
    canon_6 = abs(np.divide(float(np.subtract(feature_dictionary['eyeRight0'][0],feature_dictionary['eyeLeft3'][0])),float(np.subtract(feature_dictionary['eyeLeft3'][0],feature_dictionary['eyeLeft0'][0]))))
    canon_8 = abs(np.divide(float(np.subtract(feature_dictionary['faceContour14'][0],feature_dictionary['faceContour2'][0])),float(np.multiply(np.subtract(feature_dictionary['noseBall4'][0],feature_dictionary['noseBall0'][0]),4))))

    golden_5 = abs(np.divide(np.subtract(feature_dictionary['mouthOuter6'][0],feature_dictionary['mouthOuter0'][0]),np.multiply(np.subtract(feature_dictionary['eyeRight0'][0],feature_dictionary['eyeLeft3'][0]),1.5)))
    golden_6 = abs(np.divide(np.subtract(feature_dictionary['mouthOuter3'][1],feature_dictionary['faceContour8'][1]),np.multiply(np.subtract(feature_dictionary['eyeRight0'][0],feature_dictionary['eyeLeft3'][0]),1.5)))
    golden_7 = abs(np.divide(np.subtract(feature_dictionary['mouthOuter3'][1],feature_dictionary['faceContour8'][1]),np.multiply(np.subtract(feature_dictionary['noseBall4'][0],feature_dictionary['noseBall0'][0]),1.5)))
    golden_17 = abs(np.divide(np.subtract(feature_dictionary['mouthOuter6'][0],feature_dictionary['mouthOuter0'][0]),np.multiply(np.subtract(feature_dictionary['noseBall4'][0],feature_dictionary['noseBall0'][0]),1.5)))

    symm_1 = abs(np.divide(float(np.subtract(feature_dictionary['noseBall2'][0],feature_dictionary['mouthOuter2'][0])),float(np.subtract(feature_dictionary['eyeLeft0'][0],feature_dictionary['noseBall2'][0]))))
     
    if symm_1> 1:
        analysis.append({"recommendation":"Top lip not symmetric, left side longer than right side","description":"Apply lip liner on the inside of the left lip and outside of the right lip. Add more lipstick to the inner part of the lip.",
                   "pname":" Lip liner","productImage":"http://www.wisebread.com/files/fruganomics/u5171/city%20color.jpg"})
    elif symm_1 < 1:
        analysis.append({"recommendation":"Top lip not symmetric, left side shorter than right side","description":"Apply lip liner on the outside of the left lip and inside of the right lip. Add more lipstick to the inner part of the lip.",
                   "pname":"Lip liner","productImage":"http://www.wisebread.com/files/fruganomics/u5171/city%20color.jpg"})
    else:
        analysis.append({"recommendation":"Lips symmetric","description":"N/A",
                   "pname":"N/A","productImage":"N/A"})
    #Nose width
    if canon_8 < 1:
        analysis.append({"recommendation":"Nose width too large","description":"Perform nose contouring",
                   "pname":" Countouring powder","productImage":"http://www.wisebread.com/files/fruganomics/u5171/city%20color.jpg"})
    else:
        analysis.append({"recommendation":"Perfect Nose width","description":"N/A",
                   "pname":"N/A","productImage":"N/A"})
    #Distance between eyes   
    if canon_6 > 1:
        analysis.append({"recommendation":"Eyes too far apart","description":"Use darker eye shadow in the inner corner of the eyes and use dark brow highlights",
                   "pname":"Eye shadow and highlighter","productImage":"https://images-na.ssl-images-amazon.com/images/I/71ov2tyvmQL._SL1300_.jpg"})
    elif canon_6 < 1:
        analysis.append({"recommendation":"Eyes too close set","description":"Use lighter eye shadow in the inner corner of the eyes and use light brow highlights",
                   "pname":"Eye shadow and highlighter","productImage":"https://images-na.ssl-images-amazon.com/images/I/71ov2tyvmQL._SL1300_.jpg"})
    else:
        analysis.append({"recommendation":"Perfect eye spacing","description":"N/A",
                   "pname":"N/A","productImage":"N/A"})

    #Distance between eyes
    if golden_5 > 1:
        analysis.append({"recommendation":"Lips too wide","description":"Use lip liner inside the lips with mat lipstick",
                   "pname":"Matte lipstick","productImage":"https://www.nyxcosmetics.com/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-cpd-nyxusa-master-catalog/default/dw190a6040/ProductImages/2016/Lips/Matte_Lipstick_Extension/mattelipstick_main.jpg?sw=600&sh=600&sm=fit"})
    elif golden_5 <1: 
        analysis.append({"recommendation":"Lips too short","description":"Use lip liner outside the lips with bright lipstick",
                   "pname":"Bright lipstick","productImage":"https://darklipstips.com/wp-content/uploads/2015/08/Revlon-Super-Lustrous-Lipstick-Creme-Love-Bright-Red.jpg"})
    else :
        analysis.append({"recommendation":"Perfect lips","description":"N/A",
                   "pname":"N/A","productImage":"N/A"})

    # Mouth width 
    if canon_6 - canon_8 > 0:
        if golden_7 > 1:
            analysis.append({"recommendation":"Chin too long","description":"Perform chin contouring",
                   "pname":"","productImage":"https://media.allure.com/photos/581a4de84e15a10a15009790/master/pass/Countour-compilation.jpg"})
        else: 
            analysis.append({"recommendation":"Perfect Chin","description":"N/A",
                   "pname":"N/A","productImage":"N/A"})
    else :
        if golden_6 > 1:
            analysis.append({"recommendation":"Chin too long","description":"Perform chin contouring",
                   "pname":"N/A","productImage":"https://media.allure.com/photos/581a4de84e15a10a15009790/master/pass/Countour-compilation.jpg"})
        else :
            analysis.append({"recommendation":"Perfect Chin","description":"N/A",
                   "pname":"N/A","productImage":"N/A"})
    return analysis

@app.route('/')
def index():

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
    analyzed_json = process_json(content)
    json_return = {"data":analyzed_json}
    js = json.dumps(json_return)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(debug = True)