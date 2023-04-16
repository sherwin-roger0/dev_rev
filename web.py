import pickle
import mv_rec
import streamlit as st
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

pickle_off = open("data.pickle", 'rb')
get_rec=pickle.load(pickle_off)

title = st.text_input('Movie title')

if title:
    movies=get_rec(title)
    movies=list(movies.values)
    print(movies)

uri = "mongodb+srv://sherwinroger001:tronster@cluster0.z8w1c2a.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Data"]
Collection = db["values"]

if title:
    for i in movies:
        st.write(Collection.find_one({'id':int(i)})["original_title"],Collection.find_one({'id':int(i)})["runtime"])