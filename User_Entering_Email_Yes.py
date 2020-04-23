from Logging_Conversation import LoggingConversation



#######################################################################################################################
#######											Executing Logic
#######################################################################################################################

def UserEnteringEmailYes(req,IntentName):
    result = req.get("queryResult")
    outputContexts = result.get("outputContexts")
    email = outputContexts[1]['parameters']['email']
    print(email)
    queryTextRequest = 'User Confirmed his email with - Yes'
    queryTextResponse = {"fulfillmentMessages": [{"text": {"text": ["Thanks for confirming your email.. Please enter your phonenumber"]},"platform": "TELEGRAM"}]}

    print('User email response is:')
    print(queryTextResponse)


    LoggingConversation(queryTextRequest, queryTextResponse, IntentName,email)

    return(queryTextResponse)