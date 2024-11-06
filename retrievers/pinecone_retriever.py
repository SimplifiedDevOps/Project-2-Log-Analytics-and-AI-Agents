from pinecone import PineconeClient
from sentence_transformers import SentenceTransformer
from configparser import ConfigParser

# Load Pinecone configuration
config = ConfigParser()
config.read('../config/pinecone_config.json')
pinecone_client = PineconeClient(api_key=config['pinecone']['api_key'], environment=config['pinecone']['environment'])
index_name = config['pinecone']['index']

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_similar_logs(query_text, top_k=5):
    """
    Retrieve logs from Pinecone that are semantically similar to the query text.
    
    Parameters:
        query_text (str): The natural language query text.
        top_k (int): Number of top matches to retrieve.
    """
    query_embedding = model.encode(query_text).tolist()
    response = pinecone_client.query(
        index=index_name,
        top_k=top_k,
        vector=query_embedding,
        include_metadata=True
    )
    return [{"id": match["id"], "score": match["score"]} for match in response['matches']]
