
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sherwinroger001:tronster@cluster0.z8w1c2a.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Data"]
Collection = db["values"]

with open('movies.json') as file:
    file_data = json.load(file)

for i in range(0,4800):
    Collection.insert_one({"id":file_data["id"][str(i)],"original_title":file_data["original_title"][str(i)],"popularity":file_data["popularity"][str(i)],"runtime":file_data["runtime"][str(i)],"vote_count":file_data["vote_count"][str(i)]})

