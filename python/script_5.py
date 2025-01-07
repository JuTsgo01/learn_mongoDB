#%%
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os
pd.set_option('display.max_columns', None)
#%%
load_dotenv()

uri = os.getenv('URI')
client = MongoClient(uri)
database = client['Aula']
collection = database.get_collection("clientes")

#%%

def lendo_mongo(db_name, collection_name, columns_exc=None, query=None, MONGODB_URI=os.getenv('URI')):
    client = MongoClient(MONGODB_URI) #URI é a string de acesso ao banco
    db = client.get_database(db_name) #Nome do database do MongoDb
    collection = db.get_collection(collection_name) #Nome da collection que está no db e você usará
    
    data = collection.find()
    df = pd.DataFrame(data)
    return df

def get_endereco_df(df):
    
    if "endereco" in df.columns:
        
        df_endereco = pd.json_normalize(df['endereco'])
        df_endereco['_id'] = df['_id']
        df_cadastros = df.drop('endereco', axis=1)
        
    return df_endereco, df_cadastros

    
df_sem_tratar = lendo_mongo(
    columns_exc={}, #columns_exc é as colunas que desejo ou não desejo na consulta
    db_name="Aula", #Nome do DB que usaremos
    collection_name="clientes" #nome da collections que tem no banco e usaremos
)
    
get_endereco_df(df_sem_tratar)[0]