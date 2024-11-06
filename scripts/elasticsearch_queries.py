from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch(["http://localhost:9200"])
index_name = "java-logs"

# Function to query recent errors
def get_recent_errors():
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"log_level": "ERROR"}},
                    {"range": {"timestamp": {"gte": "now-1d/d", "lt": "now"}}}
                ]
            }
        }
    }
    return es.search(index=index_name, body=query)

# Function to query logs with a specific error code
def get_logs_by_error_code(error_code):
    query = {
        "query": {
            "term": {"error_code": error_code}
        }
    }
    return es.search(index=index_name, body=query)

# Sample usage
if __name__ == "__main__":
    print("Recent Errors:", get_recent_errors())
    print("Logs for Error Code 12345:", get_logs_by_error_code("12345"))
