def upsert_embedding_to_pinecone(pinecone_client, log_id, embedding):
    """
    Upserts a log embedding into Pinecone.
    
    Parameters:
        pinecone_client (PineconeClient): The Pinecone client instance.
        log_id (str): Unique identifier for the log entry.
        embedding (list): Embedding vector for the log entry.
    """
    vector_index = "log-embeddings"
    pinecone_client.upsert(
        index=vector_index,
        vectors=[{"id": log_id, "values": embedding}]
    )
    print("Embedding stored in Pinecone for log:", log_id)
