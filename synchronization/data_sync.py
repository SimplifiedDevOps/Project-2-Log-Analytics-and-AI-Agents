import time
from datetime import datetime
from elasticsearch import Elasticsearch
from pinecone import PineconeClient
from sentence_transformers import SentenceTransformer
from configparser import ConfigParser

# Load configurations
config = ConfigParser()
config.read('../config/elasticsearch_config.json')
pinecone_config = ConfigParser()
pinecone_config.read('../config/pinecone_config.json')

# Initialize Elasticsearch and Pinecone clients
es = Elasticsearch([config['elasticsearch']['url']])
pinecone_client = PineconeClient(api_key=pinecone_config['pinecone']['api_key'], environment=pinecone_config['pinecone']['environment'])
model = SentenceTransformer('all-MiniLM-L6-v2')

# Index and vector index names
index_name = config['elasticsearch']['index']
vector_index_name = pinecone_config['pinecone']['index']

def sync_new_logs():
    """
    Continuously checks for new logs and synchronizes them to Elasticsearch and Pinecone.
    """
    while True:
        # Retrieve new logs from a hypothetical source
        new_logs = retrieve_new_logs()  # Replace with actual log retrieval logic

        for log in new_logs:
            # Step 1: Index the log in Elasticsearch
            es.index(index=index_name, body=log)

            # Step 2: Encode log message and store embedding in Pinecone
            embedding = model.encode(log['message']).tolist()
            pinecone_client.upsert(
                index=vector_index_name,
                vectors=[{"id": log["id"], "values": embedding}]
            )

        print(f"Synced {len(new_logs)} new logs at {datetime.now()}")

        # Sync interval (e.g., 60 seconds)
        time.sleep(60)

def retrieve_new_logs():
    """
    Placeholder function to retrieve new logs from a source.
    Implement logic here to pull logs from a data source or API.
    """
    # Example logs for demonstration; replace with actual retrieval code
    return [
        {"id": "unique_log_id", "message": "New error in system", "timestamp": datetime.now().isoformat(), "log_level": "ERROR"}
    ]
