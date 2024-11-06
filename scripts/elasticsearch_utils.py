def index_log_in_elasticsearch(es_client, log):
    """
    Indexes log data into Elasticsearch.
    
    Parameters:
        es_client (Elasticsearch): The Elasticsearch client instance.
        log (dict): Log data to be indexed.
    """
    index_name = "java-logs"
    res = es_client.index(index=index_name, body=log)
    print("Log indexed in Elasticsearch:", res['result'])
