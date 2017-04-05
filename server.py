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
db = client.meme_yojna


ph = PasswordHasher()

app = Flask(__name__)


#Configuring where photos should be uploaded.
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'


@app.route('/')
def home():
	db.memes.find()
	return render_template('home.html')

@app.route('/add', methods=['GET','POST'])
def add_meme():

	if request.method == 'POST':

		filename = photos.save(request.files['meme'])
		meme = {
		'meme': filename,
		'approved': 'false',
		'approved_by': None,
		'when_uploaded':
		}
		db.memes.insert_one(meme)
		meme = db.memes.find_one({'meme':filename})
		return redirect('/%s'%(meme['_id']))
	return render_template('add_meme.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
	return render_template('admin.html')

@app.route('/<id>')
def individual_meme(id):
	meme = db.memes.find_one({'_id': ObjectId(id)})
	return render_template('individual_meme.html', meme=meme)
	



if __name__ == "__main__":
	configure_uploads(app, photos)
	app.run(debug=True, host='0.0.0.0',port=5000)