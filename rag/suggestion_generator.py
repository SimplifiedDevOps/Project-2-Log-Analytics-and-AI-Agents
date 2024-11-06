from retrievers.elasticsearch_retriever import retrieve_logs_by_level, retrieve_logs_by_date
from retrievers.pinecone_retriever import retrieve_similar_logs
from datetime import datetime, timedelta

def generate_suggestions(query, user_id):
    """
    Generate context-aware suggestions using RAG by combining data
    from Elasticsearch and Pinecone.

    Parameters:
        query (str): The operator's query.
        user_id (str): Unique identifier for the user (for memory).

    Returns:
        dict: A response containing suggested actions and insights.
    """
    # Retrieve related logs from Elasticsearch for structured data
    current_time = datetime.now().strftime("%Y-%m-%d")
    es_logs = retrieve_logs_by_date(current_time, current_time)
    
    # Retrieve similar incidents from Pinecone for semantic data
    pinecone_logs = retrieve_similar_logs(query)

    # Combine both Elasticsearch and Pinecone results for contextual insights
    suggestions = []
    for log in es_logs:
        if "ERROR" in log.get("log_level", ""):
            suggestions.append(f"Check recent error: {log['message']} on {log['timestamp']}")
    
    for incident in pinecone_logs:
        suggestions.append(f"Similar issue detected: Incident ID {incident['id']}")

    # Create response with actionable insights
    response = {
        "query": query,
        "structured_insights": es_logs,
        "semantic_insights": pinecone_logs,
        "suggestions": suggestions,
        "recommended_actions": "Refer to similar incidents and monitor logs for recurring errors."
    }

    return response
