#%%
#Inserindo dados no MongoDB diretamento do retorno da api, ou seja, diretamento de dados não estruturados
#Ou seja, aqui os dados vem como queremos e precisamos para inserir em um DB não estruturados

from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os
import requests

load_dotenv()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
load_dotenv()

#%%
def conexao_mongodb(db_name, collection_name, data_insert=None, columns_exc=None, query=None, MONGODB_URI=os.getenv('URI')):
    client = MongoClient(MONGODB_URI) #URI é a string de acesso ao banco
    db = client.get_database(db_name) #Nome do database do MongoDb
    collection = db.get_collection(collection_name) #Nome da collection que está no db e você usará
    collection.delete_many({}) #Deletando antes para toda vez que inserirmos o que vem da api, não duplicar o que já existe
    collection.insert_many(data_insert) #Inserindo dados
#%%

def get_api(api: str) -> pd.DataFrame:
    try:
        response = requests.get(api)
        if response.status_code == 200:
            return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")  
        return None

#%%   
 
mapeamendo_db = conexao_mongodb(
    db_name="IBGE", #Nome do DB que usaremos
    collection_name="distritos", #nome da collections que tem no banco e usaremos
    data_insert = get_api(os.getenv('API2')) #dados que iremos inserir no banco de dados
)

#%%

