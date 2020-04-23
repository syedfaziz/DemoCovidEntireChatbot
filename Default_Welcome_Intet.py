from Logging_Conversation import LoggingConversation





def DefaultWelcomeIntent(req,IntentName):
	result=req.get("queryResult")
	parameters=result.get("parameters")
	queryTextRequest = result.get("queryText")
	queryTextResponse = {"fulfillmentMessages": [{"image": {"imageUri": "https://www.coywolf.news/wp-content/uploads/2020/03/coronaviruse.png"},"platform": "TELEGRAM"},{"text": {"text": ["Hey there!!  \n I am your personal assistant and will assist you with details on covid-19. \n But before that I would like to have some information from you. \n Please enter your name"]      },"platform": "TELEGRAM"}]}

	LoggingConversation(queryTextRequest, queryTextResponse,IntentName,None)

	return(queryTextResponse)
