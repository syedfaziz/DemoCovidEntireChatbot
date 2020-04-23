import pymongo
import urllib
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from sendEmail import EmailSender




#### logging the conversation in mongoDB
def LoggingConversation(queryTextRequest, queryTextResponse, IntentName, CustomDetail):
    load_dotenv()
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    MyClient = pymongo.MongoClient("mongodb+srv://{}:".format(DB_USERNAME) + urllib.parse.quote(
        "{}".format(DB_PASSWORD)) + "@myfirstcluster-etywx.mongodb.net/test?retryWrites=true&w=majority")
    MyDB = MyClient.TestCovid19
    MyCollection = MyDB.UserConversation

    if IntentName == 'Default Welcome Intent':
        MyCollection.insert_one({"conversation": []})

    for document in MyCollection.find({}, sort=[('_id', pymongo.DESCENDING)]).limit(1):
        DocumentId = document['_id']

    MyCollection.update({"_id": ObjectId(DocumentId)}, {
        "$addToSet": {"conversation": [{"UserAsk": queryTextRequest, "ComputerAnswer": queryTextResponse}]}},
                        multi=True)

    if IntentName == 'UserEnteringName - yes':
        MyCollection.update({"_id": ObjectId(DocumentId)}, {"$set": {"user_name": CustomDetail}},multi=True)

    if IntentName == 'UserEnteringEmail - yes':
        MyCollection.update({"_id": ObjectId(DocumentId)}, {"$set": {"email": CustomDetail}},multi=True)

    if IntentName == 'UserEnteringPhone - yes':
        MyCollection.update({"_id": ObjectId(DocumentId)}, {"$set": {"phone": CustomDetail}},multi=True)

    if IntentName == 'UserEnteringZip':
        MyCollection.update({"_id": ObjectId(DocumentId)}, {"$set": {"zipcode": CustomDetail}},multi=True)

    if IntentName == 'CountryStatsCovid':
        for document in MyCollection.find({"_id": ObjectId(DocumentId)}):
            print(document['email'])
            recepient_email=document['email']
            send_email=EmailSender()
            send_email.send_email_to_user(recepient_email)

    MyClient.close()

