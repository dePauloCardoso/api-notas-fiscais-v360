import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

class TaxDocumentAPI:
    def __init__(self):
        load_dotenv()  # Carregar variáveis do .env
        self.api_url = os.getenv('API_URL')
        self.authorization = os.getenv('API_AUTHORIZATION')
        self.processed_ids = []

    def fetch_tax_documents(self):
        hoje = datetime.now()
        ontem = hoje - timedelta(days=1)
        data_ontem = ontem.strftime("%Y-%m-%d")
        url = f"{self.api_url}{data_ontem}"
        
        headers = {'Authorization': self.authorization}
        while url:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                dados = response.json()
                if 'payload' in dados and 'tax_documents' in dados['payload']:
                    self._process_documents(dados['payload']['tax_documents'])
                url = dados.get('next_url') if dados.get('has_more_data') else None
            else:
                print(f"Erro ao buscar documentos: {response.status_code}")
                break

    def _process_documents(self, documents):
        for doc in documents:
            if doc.get('model_type') == 'nfe' and \
               doc.get('customer_identification_number') in ['25174365000244', '25174365000406']:
                id = doc['id']
                if id not in self.processed_ids:
                    self.processed_ids.append(id)
        
        if not self.processed_ids:
            print("Nenhum novo ID para processar.")
        else:
            print(f"Total de novos IDs para processar: {len(self.processed_ids)}")

    def fetch_data_by_id(self, id):
        nova_url = f"https://arco.virtual360.io/nf/api/v2/tax_documents/{id}"
        headers = {'Authorization': self.authorization}
        response = requests.get(nova_url, headers=headers)
        if response.status_code == 200:
            novos_dados = response.json()
            return novos_dados['payload']['tax_document']
        else:
            print(f"Erro ao buscar dados do ID {id}: {response.status_code}")
            return None
