import pymongo
import json
from pymongo import MongoClient, errors
from urllib.parse import quote_plus
from pprint import pprint
import time

conn = pymongo.MongoClient("mongodb+srv://Esme:AsZx34690@cluster0.8zqs4.gcp.mongodb.net/PetCam?retryWrites=true&w=majority")
try:
    db = conn.PetCam
    collection = db.records
except AttributeError as error:
    print ("Get MongoDB database and collection ERROR:", error)

try:
    one_doc= collection.find_one()
    print ("nfind_one():", one_doc)
except errors.ServerSelectionTimeoutError as err:
    print ("nfind_one() ERROR:", err)



with open("file.txt") as f:
    for line in f:
        title, desc = line.strip().split(" ", maxsplit=1) 
        print("time: ",title, "object: ",desc)
        collection.insert_one({"user_id": "aaa", "time":title, "link": desc})
