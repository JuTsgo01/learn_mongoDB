#%%
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv('URI')
client = MongoClient(uri)
#conectando no DB
database = client.get_database("Aula")
#Usando a collection do DB
collection = database.get_collection("anac")

filtro = {"UF":"MG"}

#Colunas que não exebiremos/filtraremos
#Nunca misturar '0' com '1', pois se não iremos exibir uma, todas outras serão exibidas
#Se eu usar 1, todas as outras não serão exibidas
columns_exc = {"Numero_da_Ocorrencia":1}


#interando em cada linha do DB e aplicando filtro
for linha in collection.find(filtro, columns_exc):
    print(linha)
