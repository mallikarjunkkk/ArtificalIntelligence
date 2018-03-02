from __future__ import print_function
from flask import Flask,request
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3


app = Flask(__name__)

@app.route('/recog',methods=['POST'])
def recog():
    test_url=request.json['input']
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='xxxxxxxxxxxxxxxxxxxxxxxxx')
    url_result = visual_recognition.classify(parameters=json.dumps({'url': test_url}))
    result = json.dumps(url_result, indent=2)
    return result

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)

