#######################################################################################################################
#######											IMPORT OF LIBRARIES
#######################################################################################################################

### importing default libraries
import json 										#to convert list and dictionary to json
# import requests
from flask import Flask 							#it is microframework to develop a web app
from flask import request
from flask import make_response
import os
from dotenv import load_dotenv
# import pymongo
# import urllib
# from bson.objectid import ObjectId

### Importing custome libraries
from Default_Welcome_Intet import DefaultWelcomeIntent
from Country_Stats_Covid import CountryStatsCovid
from User_Entering_Name_Yes import UserEnteringNameYes
from User_Entering_Email_Yes import UserEnteringEmailYes
from User_Entering_Phone_Yes import UserEnteringPhoneYes
from User_Entering_Zip import UserEnteringZip

#######################################################################################################################
#Falsk app for our web app
app=Flask(__name__)


#######################################################################################################################
#######											Main Route
#######################################################################################################################

# app route decorator. when webhook is called, the decorator would call the functions which are e defined
# @app.route('/webhook', methods=['POST'])
@app.route('/', methods=['POST'])
def webhook(): 
	# convert the data from json. 
	req=request.get_json(silent=True, force=True)
	req2=req.get("queryResult")
	intent = req2.get("intent")
	# print(intent)
	IntentName = intent.get("displayName")

	if IntentName=='Default Welcome Intent':
		res=DefaultWelcomeIntent(req,IntentName)
		res=json.dumps(res, indent=4)
		r=make_response(res)
		r.headers['Content-Type']='application/json'
		return r

	elif IntentName=='CountryStatsCovid':
		res = CountryStatsCovid(req,IntentName)
		res = json.dumps(res, indent=4)
		r = make_response(res)
		r.headers['Content-Type'] = 'application/json'
		return r

	elif IntentName=='UserEnteringName - yes':
		res = UserEnteringNameYes(req,IntentName)
		res = json.dumps(res, indent=4)
		r = make_response(res)
		r.headers['Content-Type'] = 'application/json'
		return r

	elif IntentName=='UserEnteringEmail - yes':
		res = UserEnteringEmailYes(req,IntentName)
		res = json.dumps(res, indent=4)
		r = make_response(res)
		r.headers['Content-Type'] = 'application/json'
		return r

	elif IntentName=='UserEnteringPhone - yes':
		res = UserEnteringPhoneYes(req,IntentName)
		res = json.dumps(res, indent=4)
		r = make_response(res)
		r.headers['Content-Type'] = 'application/json'
		return r

	elif IntentName=='UserEnteringZip':
		res = UserEnteringZip(req,IntentName)
		res = json.dumps(res, indent=4)
		r = make_response(res)
		r.headers['Content-Type'] = 'application/json'
		return r
	else:
		return {"fulfillmentMessages": [{"text": {"text": ['IntentNotHandled']},"platform": "TELEGRAM"}]}



#######################################################################################################################
#######											Executing App
#######################################################################################################################

if __name__=='__main__':
	port=int(os.getenv('PORT',5000))
	print("starting on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
	# app.run(port=5000, debug=True)