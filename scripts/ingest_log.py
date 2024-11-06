from datetime import datetime
from elasticsearch import Elasticsearch
from pinecone import PineconeClient
from sentence_transformers import SentenceTransformer
from configparser import ConfigParser
import json
from elasticsearch_utils import index_log_in_elasticsearch
from pinecone_utils import upsert_embedding_to_pinecone

# Load configuration
config = ConfigParser()
config.read('../config/elasticsearch_config.json')

# Initialize clients
es = Elasticsearch([config['elasticsearch']['url']])
pinecone_client = PineconeClient(api_key=config['pinecone']['api_key'], environment=config['pinecone']['environment'])
model = SentenceTransformer('all-MiniLM-L6-v2')

# Ensure Pinecone index exists
vector_index = config['pinecone']['index']
if vector_index not in pinecone_client.list_indexes():
    pinecone_client.create_index(vector_index, dimension=384)

# Sample log data
logs = [
    {"id": "1", "message": "User login failed due to invalid credentials", "level": "ERROR"},
    {"id": "2", "message": "User successfully registered", "level": "INFO"},
    {"id": "3", "message": "Database connection timeout", "level": "WARNING"}
]

# Ingest logs
for log in logs:
    log['timestamp'] = datetime.now()
    index_log_in_elasticsearch(es, log)
    embedding = model.encode(log['message']).tolist()
    upsert_embedding_to_pinecone(pinecone_client, log['id'], embedding)
