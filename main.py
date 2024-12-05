from TaxDocumentAPI import TaxDocumentAPI
from DatabaseHandler import DatabaseHandler

class TaxDocumentProcessor:
    def __init__(self):
        self.api_handler = TaxDocumentAPI()
        self.db_handler = DatabaseHandler()

    def process_documents(self):
        self.api_handler.fetch_tax_documents()
        
        all_data = []
        for id in self.api_handler.processed_ids:
            tax_document = self.api_handler.fetch_data_by_id(id)
            if tax_document:
                # Informações gerais da nota fiscal
                tax_info = {
                    'id': tax_document.get('id'),
                    'number': tax_document.get('number'),
                    'total_value': float(tax_document.get('total_value', 0)),
                    'issue_date': tax_document.get('issue_date'),
                    'supplier_identification_number': tax_document.get('supplier_identification_number'),
                    'supplier_legal_name': tax_document.get('supplier_legal_name'),
                    'customer_identification_number': tax_document.get('customer_identification_number'),
                    'customer_legal_name': tax_document.get('customer_legal_name'),
                }

                # Processar todos os itens da nota fiscal
                invoice_items = tax_document.get('invoice_items', [])
                if invoice_items:
                    for item in invoice_items:
                        item_info = {
                            'item_code': item.get('item_code'),
                            'description': item.get('description'),
                            'quantity': int(float(item.get('quantity', 0))),
                            'unit_price': float(item.get('unit_price', 0)),
                            'total_value': float(item.get('total_value', 0))
                        }
                        # Combinar informações da nota fiscal com informações do item
                        all_data.append({**tax_info, **item_info})
                else:
                    # Adicionar uma entrada mesmo se não houver itens na nota
                    all_data.append(tax_info)

        # Agora inserimos os novos dados no banco
        if all_data:
            self.db_handler.insert_new_data(all_data)
        else:
            print("Nenhum dado para processar.")

if __name__ == "__main__":
    processor = TaxDocumentProcessor()
    processor.process_documents()
