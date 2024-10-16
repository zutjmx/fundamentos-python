import os
from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient(os.environ["ASTRA_DB_APPLICATION_TOKEN"])
db = client.get_database_by_api_endpoint(
  os.environ["ASTRA_DB_API_ENDPOINT"]
)

print(f"* Base de Datos: {db.info().name}\n")

print(f"Connected to Astra DB: {db.list_collection_names()}")
