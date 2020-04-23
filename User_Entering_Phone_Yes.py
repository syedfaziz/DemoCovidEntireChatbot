from Logging_Conversation import LoggingConversation



#######################################################################################################################
#######											Executing Logic
#######################################################################################################################

def UserEnteringPhoneYes(req,IntentName):
    result = req.get("queryResult")
    outputContexts = result.get("outputContexts")
    phonenumber = outputContexts[1]['parameters']['phone-number']
    print(phonenumber)
    queryTextRequest = 'User Confirmed his phone-number with - Yes'
    queryTextResponse = {"fulfillmentMessages": [{"text": {"text": ["Thanks for confirming your phone-number.. Please enter your ZipCode"]},"platform": "TELEGRAM"}]}

    print('User email response is:')
    print(queryTextResponse)


    LoggingConversation(queryTextRequest, queryTextResponse, IntentName,phonenumber)

    return(queryTextResponse)