#%%
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os
import requests

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
load_dotenv()

url = os.getenv('API2')

#%%

def get_api(api: str) -> pd.DataFrame:
    try:
        response = requests.get(api)
        if response.status_code == 200:
            df_data = pd.DataFrame(response.json())
            return df_data
        
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
            
        return df_all_columns
    else:
        print("Erro ou tentar normalizar o arquivo, pois a coluna 'nome' não existe")
        return None
    
    
data = get_api(url)
df_normalize(data).head()

#%%
