import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# Função para obter variáveis de ambiente com valor padrão
def get_env(key, default=None):
    value = os.getenv(key)
    return default if value is None else value

# Obtém as variáveis de ambiente
DB_HOST = get_env('DB_HOST_PROD', 'localhost')
DB_PORT = int(get_env('DB_PORT_PROD', '5432'))  # Converte para int e usa 5432 como padrão
DB_NAME = get_env('DB_NAME_PROD', 'database')
DB_USER = get_env('DB_USER_PROD', 'user')
DB_PASS = get_env('DB_PASS_PROD', 'password')
DB_SCHEMA = get_env('DB_SCHEMA_PROD', 'public')

# URL de conexão do banco de dados
DATA_BASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f"URL de conexão: {DATA_BASE_URL}")

# Criando a engine
engine = create_engine(DATA_BASE_URL)

# Lendo dados da tabela bruta
df_raw = pd.read_sql('''
                     WITH tratativa_scrapy AS (
    SELECT
        brand AS marca_produto,
        name AS nome_produto,
        COALESCE(reviews_rating_number, 0) AS avaliacoes_produto,
        COALESCE(CAST(REGEXP_REPLACE(review_amount, '[()]', '', 'g') AS INT), 0) AS avaliacoes_total_tratadas,
        CAST(CONCAT(
            REPLACE(old_price::VARCHAR(5), '.', ''), '.',
            old_price_cents) AS DECIMAL) AS preco_anterior_tratado,
        CAST(CONCAT(
            REPLACE(new_price::VARCHAR(5), '.', ''), '.',
            new_price_cents) AS DECIMAL) AS preco_novo_tratado,
        DATE(NOW()) AS data_ref
    FROM
        tbl_results_scraping trs
)
SELECT * FROM tratativa_scrapy;
''', engine)

# Adicionar a coluna id_produto
df_raw['id_produto'] = range(1, len(df_raw) + 1)

# Obtém as variáveis de ambiente para o segundo banco de dados
DB_HOST_2 = get_env('DB_HOST_PROD_2', 'localhost')
DB_PORT_2 = int(get_env('DB_PORT_PROD_2', '4352'))
DB_NAME_2 = get_env('DB_NAME_PROD_2', 'database')
DB_USER_2 = get_env('DB_USER_PROD_2', 'user')
DB_PASS_2 = get_env('DB_PASS_PROD_2', 'password')
DB_SCHEMA_2 = get_env('DB_SCHEMA_PROD_2', 'public')

# URL de conexão do segundo banco de dados
DATA_BASE_URL_2 = f"postgresql://{DB_USER_2}:{DB_PASS_2}@{DB_HOST_2}:{DB_PORT_2}/{DB_NAME_2}"

print(f"URL de conexão 2: {DATA_BASE_URL_2}")

# Criando a engine para o segundo banco de dados
engine_2 = create_engine(DATA_BASE_URL_2)

# Preparando o DataFrame final
final_df = df_raw

Base = declarative_base()

# Definindo a tabela
class DWResultsScrapy(Base):
    __tablename__ = 'DW_RESULTS_SCRAPY'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    marca_produto = Column(String, nullable=False)
    nome_produto = Column(String, nullable=False)
    avaliacoes_produto = Column(Integer, nullable=True)
    avaliacoes_total_tratadas = Column(Integer, nullable=True)
    preco_anterior_tratado = Column(Float, nullable=False)
    preco_novo_tratado = Column(Float, nullable=True)
    data_ref = Column(Date, nullable=False)

def salvar_bd(final_df, engine, schema='public'):
    try:
        Base.metadata.create_all(engine)
        
        # Obter as colunas da classe DWResultsScrapy
        colunas_ordenadas = [column.name for column in DWResultsScrapy.__table__.columns]
        
        # Reordenar as colunas do DataFrame
        final_df = final_df[colunas_ordenadas]
        
        final_df.to_sql('DW_RESULTS_SCRAPY', engine, schema=schema, if_exists='replace', index=False)
        print('Dados salvos com sucesso no banco de dados!')
    except Exception as e:
       print(f'Erro ao salvar os dados: {str(e)}')

if __name__ == '__main__':
    salvar_bd(final_df, engine_2, schema=DB_SCHEMA_2)
