#Inserindo dados a partir de uma tranformação de dados estruturados em dados não estruturados para enserir no MongoDB
#Aqui estamos fazendo um caminho contrário do que fariamos em um SQL
#Partindo de um dados estruturado, tranformando em não estruturados e inserindo

#%%
#Inserindo dados no MongoDB diretamente do retorno da API - json
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
            return pd.DataFrame(response.json())
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")  
        return None

def df_normalize(df_data: pd.DataFrame) -> pd.DataFrame:
    if df_data is None or df_data.empty:
        print("Dataframe vazio")
        return None
    
    if "municipio" in df_data.columns:
        df_municipios = pd.json_normalize(df_data['municipio'], sep='_') #normalizando as colunas
        df_municipios.columns = [f"municipios_{col}" for col in df_municipios.columns] #renomeando as colunas do df normalizado para poder fazer o join dos dois df
        df_all_columns = df_data.drop(columns=['municipio']).join(df_municipios.drop(columns=['municipios_regiao-imediata_regiao-intermediaria_UF_sigla',
                                                                                              'municipios_regiao-imediata_regiao-intermediaria_UF_nome',
                                                                                              'municipios_regiao-imediata_regiao-intermediaria_UF_regiao_sigla',
                                                                                              'municipios_regiao-imediata_regiao-intermediaria_UF_regiao_nome',
                                                                                              'municipios_regiao-imediata_regiao-intermediaria_UF_id',
                                                                                              'municipios_regiao-imediata_regiao-intermediaria_UF_regiao_id']))
        for col_name in df_all_columns.columns: #Renomeando colunas
            if col_name.count('_') > 1:
                partes = col_name.split('_')
                df_all_columns = df_all_columns.rename(columns={col_name : f"{partes[-2]}_{partes[-1]}"})
            
        return df_all_columns.to_dict(orient='records')
    else:
        print("Erro ou tentar normalizar o arquivo, pois a coluna 'nome' não existe")
        return None

#%%   
mapeamendo_db = conexao_mongodb(
    db_name="IBGE", #Nome do DB que usaremos
    collection_name="distritostwo", #nome da collections que tem no banco e usaremos
    data_insert = df_normalize(get_api(os.getenv('API2')))) #dados que iremos inserir no banco de dados



#%%
