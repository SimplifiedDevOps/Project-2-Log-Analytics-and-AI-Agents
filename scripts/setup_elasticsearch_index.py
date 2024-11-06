from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch(["http://localhost:9200"])
index_name = "java-logs"

# Define index mapping
mapping = {
    "mappings": {
        "properties": {
            "timestamp": {"type": "date"},
            "log_level": {"type": "keyword"},
            "error_code": {"type": "keyword"},
            "stack_trace": {"type": "text"},
            "message": {"type": "text"},
        }
    }
}

# Create index with the defined mapping
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapping)
    print(f"Index '{index_name}' created with custom mapping.")
else:
    print(f"Index '{index_name}' already exists.")
