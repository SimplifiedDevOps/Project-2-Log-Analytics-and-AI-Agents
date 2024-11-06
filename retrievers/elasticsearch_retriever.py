from elasticsearch import Elasticsearch
from configparser import ConfigParser

# Load Elasticsearch configuration
config = ConfigParser()
config.read('../config/elasticsearch_config.json')
es = Elasticsearch([config['elasticsearch']['url']])
index_name = config['elasticsearch']['index']

def retrieve_logs_by_date(start_date, end_date):
    """
    Retrieve logs within a specific date range.
    
    Parameters:
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    """
    query = {
        "query": {
            "range": {
                "timestamp": {
                    "gte": start_date,
                    "lt": end_date
                }
            }
        }
    }
    response = es.search(index=index_name, body=query)
    return [hit['_source'] for hit in response['hits']['hits']]

def retrieve_logs_by_level(log_level):
    """
    Retrieve logs of a specific log level.
    
    Parameters:
        log_level (str): Log level to filter (e.g., "ERROR", "INFO").
    """
    query = {
        "query": {
            "term": {
                "log_level": log_level
            }
        }
    }
    response = es.search(index=index_name, body=query)
    return [hit['_source'] for hit in response['hits']['hits']]
