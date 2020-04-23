from Logging_Conversation import LoggingConversation



#######################################################################################################################
#######											Executing Logic
#######################################################################################################################

def UserEnteringZip(req,IntentName):
    result = req.get("queryResult")
    outputContexts = result.get("outputContexts")
    zipcode = outputContexts[1]['parameters']['zip-code']
    print(zipcode)
    queryTextRequest = 'User Confirmed his Zip-Code with - Yes'
    queryTextResponse = {"fulfillmentMessages": [{"text": {"text": ["Thanks for confirming your zip-code.. Please enter the country name for which you want to see the Covid-19 Stats"]},"platform": "TELEGRAM"}]}

    print('User zip  response is:')
    print(queryTextResponse)


    LoggingConversation(queryTextRequest, queryTextResponse, IntentName,zipcode)

    return(queryTextResponse)