# Tax Document Processor

Este projeto é responsável por processar documentos fiscais eletrônicos, coletando dados de uma API e armazenando-os em um banco de dados PostgreSQL. Ele realiza as seguintes tarefas:

1. **Coleta de documentos fiscais** através de uma API.
2. **Extração de dados** dos documentos fiscais (incluindo informações de itens de cada nota fiscal).
3. **Armazenamento dos dados** em um arquivo CSV.
4. **Inserção dos dados no banco de dados PostgreSQL**, incluindo a filtragem para evitar duplicação de registros.

## Estrutura do Projeto

O projeto é dividido em três arquivos principais, cada um com uma responsabilidade específica:

- `Main.py`: O arquivo principal, que executa o fluxo do processo, que inclui a coleta dos documentos fiscais, processamento dos dados e inserção no banco de dados.
- `TaxDocumentAPI.py`: Contém a lógica de interação com a API de documentos fiscais. Aqui são feitas as requisições HTTP e o processamento dos dados dos documentos.
- `DatabaseHandler.py`: Responsável pela manipulação do banco de dados, incluindo a conexão ao banco PostgreSQL e a inserção dos dados.

## Pré-requisitos

Antes de rodar o projeto, você precisará de:

- Python 3.x
- Bibliotecas Python: `requests`, `pandas`, `sqlalchemy`
- Acesso a um banco de dados PostgreSQL configurado
- Arquivo `.env` com as credenciais para autenticação da API e banco de dados

### Instalar Dependências

Para instalar as dependências necessárias, execute o seguinte comando:

```bash
pip install requests pandas sqlalchemy 
```

## Configuração

### Arquivo `.env`

Certifique-se de criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:

- API_USERNAME=your_api_username
- API_PASSWORD=your_api_password
- DB_USER=your_db_user
- DB_PASSWORD=your_db_password
- DB_HOST=localhost
- DB_PORT=5432
- DB_NAME=your_db_name


# Banco de Dados PostgreSQL
Antes de rodar o script, verifique se o banco de dados PostgreSQL está configurado corretamente com a tabela notas_sae_raw. O código realiza a inserção dos dados nesta tabela.

# Como Usar
Executar o Processo Completo
Para rodar o script e processar os documentos fiscais, basta executar o arquivo Main.py:

```bash
python main.py
```

Isso irá:

1. Buscar os documentos fiscais a partir da API.
2. Processar os dados e extrair as informações relevantes.
3. Armazenar os dados extraídos em um arquivo CSV.
4. Verificar quais dados ainda não estão no banco de dados e inserir os novos registros.
# Processamento de Dados
O fluxo de processamento é o seguinte:

1. A classe TaxDocumentAPI faz requisições para a API de documentos fiscais e armazena os documentos encontrados.
2. Os documentos são analisados, e os dados, como informações gerais da nota fiscal e itens de cada nota fiscal, são extraídos.
3. A classe DatabaseHandler verifica quais documentos já estão presentes no banco de dados, evitando a duplicação.
4. Os novos documentos são inseridos no banco de dados PostgreSQL.

# Exemplo de Saída
Após a execução, os novos dados serão inseridos no banco de dados e, se houver dados novos, você verá a seguinte mensagem no console:


```bash
Novos dados inseridos no banco de dados com sucesso!
```
Se não houver dados novos para processar, a seguinte mensagem será exibida:

```bash
Nenhum dado novo encontrado para inserir no banco de dados.
```
# Arquivos Importantes
- Main.py: Controla o fluxo de execução principal do projeto.
- TaxDocumentAPI.py: Interage com a API para buscar os documentos fiscais.
- DatabaseHandler.py: Lida com a conexão e manipulação do banco de dados.

# Contribuindo
Se você quiser contribuir para o projeto, sinta-se à vontade para abrir um Pull Request. Certifique-se de que suas alterações estão bem testadas e documentadas.

# Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.# api-notas-fiscais-v360
