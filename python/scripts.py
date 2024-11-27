#%%
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os
#%%
load_dotenv()

uri = os.getenv('URI')
client = MongoClient(uri)
database = client.get_database("Aula")
collection = database.get_collection("anac")

#%%
try:

    filtro = {"Numero_da_Ocorrencia": "7526"}
    anac = collection.find_one(filtro)
    print(anac)

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)

