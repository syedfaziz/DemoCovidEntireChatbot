import json
import requests
from Logging_Conversation import LoggingConversation
import os
from dotenv import load_dotenv



#######################################################################################################################
#######											Executing Logic
#######################################################################################################################

def CountryStatsCovid(req,IntentName):
	result = req.get("queryResult")
	parameters = result.get("parameters")
	country = parameters.get("geo-country")
	print(country)
	# country = 'india'
	queryTextRequest = result.get("queryText")


	# email = parameters.get("email")
	# r=requests.get('http://api.openweathermap.org/data/2.5/forecast?q=hyderabad,in&appid=db91df44baf43361cbf73026ce5156cb')
	# url = r'https://bing.com/covid/data'
	# r = requests.get(url)
	# data = json.loads(r.text)

	url = "https://covid-193.p.rapidapi.com/statistics"

	load_dotenv()



	# headers = {
	# 	'x-rapidapi-host': "covid-193.p.rapidapi.com",
	# 	'x-rapidapi-key': "6999f8d1damsh38c931d610b352cp1fe69bjsn11d47d220dee"
	# }

	headers = {
			'x-rapidapi-host': os.getenv('x-rapidapi-host'),
			'x-rapidapi-key': os.getenv('x-rapidapi-key')
		}

	response = requests.request("GET", url, headers=headers)
	data = json.loads(response.text)

	for i in range(len(data['response'])):
		if str.lower(data['response'][i]['country']) == str.lower(country):
			totalConfirmed = 'totalConfirmed case count = {}'.format(str(data['response'][i]['cases']['total']))
			totalDeaths = 'totalDeaths case count = {}'.format(str(data['response'][i]['deaths']['total']))
			totalRecovered = 'totalRecovered case count = {}'.format(str(data['response'][i]['cases']['recovered']))
			totalConfirmedDelta = 'totalConfirmedDelta case count = {}'.format(str(data['response'][i]['cases']['new']))
			print({"fulfillmentMessages": [
				{"text": {"text": [str({'totalConfirmed': str(data['response'][i]['cases']['total']),
										'totalDeaths': str(data['response'][i]['deaths']['total']),
										'totalRecovered': str(data['response'][i]['cases']['recovered']),
										'totalConfirmedDelta': str(data['response'][i]['cases']['new'])})]}}]})

			queryTextResponse = {"fulfillmentMessages": [
				{"text": {"text": ["You world be receiving a covid-19 handbook on your email \n" + str({'totalConfirmed': str(data['response'][i]['cases']['total']),
										'totalDeaths': str(data['response'][i]['deaths']['total']),
										'totalRecovered': str(data['response'][i]['cases']['recovered']),
										'totalConfirmedDelta': str(data['response'][i]['cases']['new'])})]},"platform": "TELEGRAM"},{"quickReplies":{"title": "Do You want to see a world map overview??","quickReplies": ["Yes","No"]},"platform": "TELEGRAM"}]}

			print('countryresponsetext is:')
			print(queryTextResponse)


			LoggingConversation(queryTextRequest, queryTextResponse, IntentName,None)

			return(queryTextResponse)

	else:

		queryTextResponse= 'no such country'
		LoggingConversation(queryTextRequest, queryTextResponse,IntentName,None)
		# return('no such country')
		return {"fulfillmentMessages": [{"text": {"text": ['no such country']}}]}
