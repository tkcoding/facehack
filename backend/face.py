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
from math import sqrt,pow
from operator import itemgetter

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app,resources={r"/*": {"origins": "*"}},allow_headers='*')

print("initiated the app! With a name of:", __name__)

def facecontour_matching(face_contour):
    dia = [[0,0],[17,142],[42,277],[66,414],[112,535],[187,644],[283,737],[393,824],[520,851],[648,831],[760,748],[858,652],[934,541],[979,416],[1002,280],[1027,144],[1043,-2]]
    scale = dia[-1][0]/100;
    dia = np.divide(dia,scale)
    sq = [[0,0],[7,68],[18,136],[31,204],[55,268],[92,323],[136,372],[188,415],[247,426],[305,414],[356,369],[400,319],[435,264],[458,201],[471,133],[483,65],[489,-3]]
    scale = sq[-1][0]/100;
    sq = np.divide(sq,scale)
    ov = [[0,0],[0,15],[3,31],[5,46],[9,60],[17,71],[28,81],[40,89],[53,91],[66,89],[76,80],[85,71],[92,60],[97,48],[100,34],[102,21],[103,7]]
    scale = ov[-1][0]/100;
    ov = np.divide(ov,scale)
    ro = [[0,0],[1,31],[5,62],[8,92],[15,122],[30,148],[52,170],[77,187],[105,194],[136,192],[166,179],[194,161],[214,138],[225,109],[233,78],[241,47],[246,13]]
    scale = ro[-1][0]/100;
    ro = np.divide(ro,scale)
    he = [[0,0],[6,49],[16,97],[26,143],[44,185],[73,220],[109,251],[147,280],[188,290],[231,282],[272,254],[312,224],[342,188],[360,144],[370,96],[378,46],[384,-7]]
    scale = he[-1][0]/100;
    he = np.divide(he,scale)
    re = [[0,0],[7,68],[18,136],[31,204],[55,268],[92,323],[136,372],[188,415],[247,426],[305,414],[356,369],[400,319],[435,264],[458,201],[471,133],[483,65],[489,-3]]
    scale = re[-1][0]/100;
    re = np.divide(re,scale)

    im_cnt = np.subtract(face_contour[:],face_contour[0])
    scale = im_cnt[-1][0]/100;
    im_cnt = np.divide(im_cnt,scale)

    sqrt(np.sum(np.power(np.subtract(im_cnt,dia),2)))
    contour_type = ["diamond.png","square.png","oval.png","rectangle.png","round.png","heart.png"]
    i, value = min(enumerate([sqrt(np.sum(np.power(np.subtract(im_cnt,dia),2))),sqrt(np.sum(np.power(np.subtract(im_cnt,sq),2))),sqrt(np.sum(np.power(np.subtract(im_cnt,ov),2))),sqrt(np.sum(np.power(np.subtract(im_cnt,re),2))),sqrt(np.sum(np.power(np.subtract(im_cnt,ro),2))),sqrt(np.sum(np.power(np.subtract(im_cnt,he),2)))]), key=itemgetter(1))
    return contour_type[i]

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
    facecontour_analysis = facecontour_matching(json_result['objects'][1]['landmarks']['faceContour'])
    return analysis,facecontour_analysis

@app.route('/')
def index():

    app.logger.info('Test')
    return "Hello, World!"

app = Flask(__name__)


@app.route("/img", methods=["POST"])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def home():
    content = request.get_json()
    #img = Image.open(request.files['file'])
    # print(content,sys.stdout)
    # sys.stdout.flush()
    analyzed_json,facecontour_analysis = process_json(content)
    json_return = {"data":analyzed_json,"facecountour":facecontour_analysis}
    js = json.dumps(json_return)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(debug = True)