#%%
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


#%%
def lendo_mongo(db_name, collection_name, columns_exc=None, query=None, MONGODB_URI=os.getenv('URI')):
    client = MongoClient(MONGODB_URI) #URI é a string de acesso ao banco
    db = client.get_database(db_name) #Nome do database do MongoDb
    collection = db.get_collection(collection_name) #Nome da collection que está no db e você usará
    
    #Definindo o cursor que executará a query
    cursor = collection.find(query)
    
    #Criando um df a partir da query e retornando ele
    df = pd.DataFrame(list(cursor))
    
    return df

def df_tratado(df):
    
    if "_id" in df.columns:
        df.drop(columns=["_id"], inplace=True)
        
    if "Data_da_Ocorrencia" in df.columns:
        df['Data_da_Ocorrencia'] = pd.to_datetime(df['Data_da_Ocorrencia'])
    
    return df   

df_sem_tratar = lendo_mongo(
    query = {"Regiao":"Nordeste"}, #query é o filtro que desejo aplicar
    columns_exc={}, #columns_exc é as colunas que desejo ou não desejo na consulta
    db_name="Aula", #Nome do DB que usaremos
    collection_name="anac" #nome da collections que tem no banco e usaremos
)


df_tratado(df_sem_tratar)

#%%
