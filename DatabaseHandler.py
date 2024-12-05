import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

class DatabaseHandler:
    def __init__(self):
        load_dotenv()
        self.db_config = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'database': os.getenv('DB_NAME')
        }
        self.engine = self._create_engine()

    def _create_engine(self):
        connection_string = (f"postgresql+psycopg2://{self.db_config['user']}:{self.db_config['password']}@"
                              f"{self.db_config['host']}:{self.db_config['port']}/{self.db_config['database']}")
        return create_engine(connection_string)

    def insert_new_data(self, data):
        df_csv = pd.DataFrame(data)
        df_csv.columns = [col.strip() for col in df_csv.columns]  # Remover espaços extras nos nomes das colunas

        try:
            query = "SELECT id FROM notas_sae_raw"
            existing_ids = pd.read_sql(query, con=self.engine)
            existing_ids_set = set(existing_ids['id'].astype(str))
            new_data = df_csv[~df_csv['id'].astype(str).isin(existing_ids_set)]

            if not new_data.empty:
                new_data.to_sql('notas_sae_raw', con=self.engine, if_exists='append', index=False)
                print("Novos dados inseridos no banco de dados com sucesso!")
            else:
                print("Nenhum dado novo encontrado para inserir no banco de dados.")
        except Exception as e:
            print(f"Erro ao processar os dados: {e}")
