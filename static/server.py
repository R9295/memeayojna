from flask import Flask,render_template,redirect,request,make_response,redirect,url_for,jsonify
from pymongo import MongoClient
from argon2 import PasswordHasher
import json
#to query collections by their Id
from bson.objectid import ObjectId
from time import gmtime, strftime
import string 
import random
from time import gmtime,strftime
from flask_uploads import UploadSet, configure_uploads, IMAGES
from datetime import *
import datetime


#Connecting to DB
client = MongoClient()
db = client.neem_tree




ph = PasswordHasher()

app = Flask(__name__)


#Configuring where photos should be uploaded.
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'


@app.route('/')
def home():
	return 'XD'


if __name__ == "__main__":
	configure_uploads(app, photos)
	app.run(debug=True, host='0.0.0.0',port=5000)