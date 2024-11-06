import json
from pinecone import PineconeClient

# Load Pinecone configuration
with open('../config/pinecone_config.json') as f:
    pinecone_config = json.load(f)

# Extract Pinecone settings
api_key = pinecone_config['pinecone']['api_key']
environment = pinecone_config['pinecone']['environment']
index_name = pinecone_config['pinecone']['index_name']
namespace = pinecone_config['pinecone'].get('namespace', "")
metric = pinecone_config['pinecone']['metric']
top_k = pinecone_config['pinecone']['top_k']

# Initialize Pinecone client
pinecone_client = PineconeClient(api_key=api_key, environment=environment)

# Example function to retrieve Pinecone settings
def get_pinecone_client():
    return pinecone_client

def get_pinecone_settings():
    return {
        "index_name": index_name,
        "namespace": namespace,
        "metric": metric,
        "top_k": top_k
    }
