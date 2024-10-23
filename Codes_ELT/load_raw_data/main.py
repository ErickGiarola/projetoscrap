import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Função para obter variáveis de ambiente com valor padrão
def get_env(key, default=None):
    value = os.getenv(key)
    return default if value is None else value

# Obtém as variáveis de ambiente
DB_HOST = get_env('DB_HOST_PROD', 'localhost')
DB_PORT = int(get_env('DB_PORT_PROD', '4352'))
DB_NAME = get_env('DB_NAME_PROD', 'database')
DB_USER = get_env('DB_USER_PROD', 'user')
DB_PASS = get_env('DB_PASS_PROD', 'password')
DB_SCHEMA = get_env('DB_SCHEMA_PROD', 'public')

# URL de conexão do banco de dados
DATA_BASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f"URL de conexão: {DATA_BASE_URL}")

# Criando a engine
engine = create_engine(DATA_BASE_URL)

# Lendo o arquivo CSV
csv_file_path = r'C:\Users\erick\imdb\data\data.csv'
df = pd.read_csv(csv_file_path)

def salvar_bd(df, schema='public'):
    try:
        df.to_sql('tbl_results_scraping', engine, schema=schema, if_exists='replace', index=False)
        print('Dados salvos com sucesso no banco de dados!')
    except Exception as e:
        print(f'Erro ao salvar os dados: {str(e)}')

if __name__ == '__main__':
    salvar_bd(df, schema=DB_SCHEMA)
