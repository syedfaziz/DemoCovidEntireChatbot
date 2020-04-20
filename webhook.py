import json #to convert list and dictionary to json 
import os 
import requests 
from flask import Flask #it is microframework to develop a web app 
from flask import request
from flask import make_response

#Falsk app for our web app
app=Flask(__name__)

# app route decorator. when webhook is called, the decorator would call the functions which are e defined

# @app.route('/webhook', methods=['POST'])
@app.route('/', methods=['POST'])
def webhook(): 
	# convert the data from json. 
	req=request.get_json(silent=True, force=True)
	intent = req.get("intent")
	IntentName = intent.get("displayName")

	if IntentName=='Default Welcome Intent':
		res=DefaultWelcomeIntent(req)
		res=json.dumps(res, indent=4)
		r=make_response(res)
		r.headers['Content-Type']='application/json'
		return r
	elif IntentName=='CountryStatsCovid':
		res = CountryStatsCovid(req)
		res = json.dumps(res, indent=4)
		r = make_response(res)
		r.headers['Content-Type'] = 'application/json'
		return r
	else:
		pass

# extract parameter values, query weahter api, construct the resposne 
def DefaultWelcomeIntent(req):
	result=req.get("queryResult")
	parameters=result.get("parameters") 

	#return{ "fulfillmentMessages": [ { "text": { "text": [speech] } }]}
	#return{ "fulfillmentMessages": [ { "image": { "imageUri": [speech] } }]}
	#return{"fulfillmentMessages": [{"image": {"imageUri": "https://cdn.pixabay.com/photo/2015/06/19/21/24/the-road-815297__340.jpg"},"platform": "SLACK"}]}

	return({"fulfillmentMessages": [{"image": {"imageUri": "https://www.coywolf.news/wp-content/uploads/2020/03/coronaviruse.png"},"platform": "TELEGRAM"},{"text": {"text": ["Hey there!!  \n I am your personal assistant and will assist you with details on covid-19. \n But before that I would like to have some information from you. \n Please enter the following details : \n 	_firstname lastname_ \n 	_email_id_ \n 	_phonenumber_ \n 	_pincode_ \n"]      },"platform": "TELEGRAM"}]})
	#return{ "fulfillmentMessages": [ { "text": { "text": [IntentName] },"platform": "TELEGRAM" }]}


#######################################################################################################################

def CountryStatsCovid(req):
	result = req.get("queryResult")
	parameters = result.get("parameters")
	country = parameters.get("geo-country")
	email = parameters.get("email")
	# r=requests.get('http://api.openweathermap.org/data/2.5/forecast?q=hyderabad,in&appid=db91df44baf43361cbf73026ce5156cb')
	url = r'https://bing.com/covid/data'
	r = requests.get(url)
	data = json.loads(r.text)

	for i in range(len(data['areas'])):
		if data['areas'][i]['id'] == str.lower(country):
			# print(data['areas'][i])
			# return(data['areas'][i])
			# return {"fulfillmentMessages": [{"text": {"text": [str(data['areas'][i])]}}]}
			totalConfirmed = 'totalConfirmed case count = {}'.format(str(data['areas'][i]['totalConfirmed']))
			totalDeaths = 'totalDeaths case count = {}'.format(str(data['areas'][i]['totalDeaths']))
			totalRecovered = 'totalRecovered case count = {}'.format(str(data['areas'][i]['totalRecovered']))
			totalRecoveredDelta = 'totalRecoveredDelta case count = {}'.format(
				str(data['areas'][i]['totalRecoveredDelta']))
			totalDeathsDelta = 'totalDeathsDelta case count = {}'.format(str(data['areas'][i]['totalDeathsDelta']))
			totalConfirmedDelta = 'totalConfirmedDelta case count = {}'.format(
				str(data['areas'][i]['totalConfirmedDelta']))

			# sending email_to_user
			email_sender = EmailSender()
			email_sender.send_email_to_user(email)

			return {"fulfillmentMessages": [{"text": {"text": [str('EMAIL HAS BEEN SENT TO YOUR EMAIL_ADDRESS\n') + str(
				{'totalConfirmed': str(data['areas'][i]['totalConfirmed']),
				 'totalDeaths': str(data['areas'][i]['totalDeaths']),
				 'totalRecovered': str(data['areas'][i]['totalRecovered']),
				 'totalRecoveredDelta': str(data['areas'][i]['totalRecoveredDelta']),
				 'totalDeathsDelta': str(data['areas'][i]['totalDeathsDelta']),
				 'totalConfirmedDelta': str(data['areas'][i]['totalConfirmedDelta'])})]}}]}
	# return {"fulfillmentMessages": [{"text": {"text": ["dummy Text"]},"image": {"imageUri": "data:image/jpeg;base64,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xSH/ANR9yocuJbtLp/EJK3rpfHv2cdTx3LWs9AhPRI9axc1sXiOrlPHLPXnumAMiGptsB15qdpPS0e1x25UuO0u6u5W++RkpUokkJ8gM45VnDCGC5Gqr4jiT6h+SN1oxoB0HNXDVltrbqnUQIocUoqUvshknzJ86kyN3sqJqZyMpebDqpiGkI5IQlI/pGKyAsoi4ncr3ivV4iiLNERREURFERREURFERREURFERREURFERRFjHvoiMepoi1SIzMmO4w+gONOJKVoV0IrwgEWKyY90bg5psQldix36zt9jY7qy5ET+7ZuDZWUDyCkkHFQd3IwWYdOq2rqyjqTnqIyHcS02v7FbBE1hJG1+5WuKk9TGjrUr/kaZZzuQsDLhjD4WOd6kD6KdaNNw4En211bsy4KThUqQsrV8M8kj0FZsia03OpUNRXyzM7seFnIaf8A33V2BjpUqorNERREURFERREURFERREURFERREURFERREURFERREURFERREURYwPKiLNEWCQOtERuHnRFnNEWAQehoiAQehoiMiiLClpQMrUEjzJoix2zWcdony60RAeaIz2ifnREB1s5w4nlnPPyoi9AhQyDkGiLNERREURFERREURFERREURFERREURFERRFDmW9Etxta1qAR1SAMK5g/pRFHVZm1nvvuLAxtSsAhOM+Y9fpRFlNmbSz2fbukj+MnJznOefnREIszaFZS8sDI7u0bT7xjn0+ZJ8aIvQtSQwhn2h3agEJJxkZGPn5eVEQ1akNuocDzhUg8vLw5fT6miLc5AbcafbWtxSXl7lBatwHTkAeg5dPU0Ra1WtouBYUQe2LpwBzOMfYCiLSqxskJCXnU7EpSgpwCnHqPPrRFtXamlKKtxGSsq5DvbsfbA+VEUqIwmLHQwhRUlAxlXU0RbqIiiIoiKIiiIoiKIv/9k="},"platform": "SLACK"}]}
	else:

		print('no such country')
		# return('no such country')
		return {"fulfillmentMessages": [{"text": {"text": ['no such country']}}]}






#######################################################################################################################
if __name__=='__main__':
	port=int(os.getenv('PORT',5000))
	print("starting on port %d" % port)
	app.run(debug=True, port=port, host='0.0.0.0')
	# app.run(port=5000, debug=True)