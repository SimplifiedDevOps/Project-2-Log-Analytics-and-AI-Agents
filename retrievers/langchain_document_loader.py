from retrievers.elasticsearch_retriever import retrieve_logs_by_date, retrieve_logs_by_level
from retrievers.pinecone_retriever import retrieve_similar_logs

def load_and_format_logs(query_type, query_params):
    """
    Loads and formats logs from Elasticsearch and Pinecone for a unified result set.
    
    Parameters:
        query_type (str): Type of query ('date', 'level', or 'semantic').
        query_params (dict): Parameters for the query (e.g., date range, log level, or query text).
    
    Returns:
        dict: Structured logs from Elasticsearch and/or Pinecone.
    """
    results = {}

    if query_type == 'date':
        start_date = query_params.get("start_date")
        end_date = query_params.get("end_date")
        es_logs = retrieve_logs_by_date(start_date, end_date)
        results["elasticsearch"] = es_logs

    elif query_type == 'level':
        log_level = query_params.get("log_level")
        es_logs = retrieve_logs_by_level(log_level)
        results["elasticsearch"] = es_logs

    elif query_type == 'semantic':
        query_text = query_params.get("query_text")
        pinecone_logs = retrieve_similar_logs(query_text)
        results["pinecone"] = pinecone_logs

    return results
