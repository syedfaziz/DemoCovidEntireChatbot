# import json
# import requests
from Logging_Conversation import LoggingConversation
# import os
# from dotenv import load_dotenv



#######################################################################################################################
#######											Executing Logic
#######################################################################################################################

def UserEnteringNameYes(req,IntentName):
    result = req.get("queryResult")
    outputContexts = result.get("outputContexts")
    user_name = outputContexts[1]['parameters']['user-name']
    print(user_name)
    queryTextRequest = 'User Confirmed his name with - Yes'
    queryTextResponse = {"fulfillmentMessages": [{"text": {"text": ["Thanks for confirming your name.. PLease enter your email"]},"platform": "TELEGRAM"}]}

    print('User name response is:')
    print(queryTextResponse)


    LoggingConversation(queryTextRequest, queryTextResponse, IntentName,user_name)

    return(queryTextResponse)