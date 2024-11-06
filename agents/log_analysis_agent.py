
import json
from elasticsearch import Elasticsearch
from pinecone import PineconeClient
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from sentence_transformers import SentenceTransformer
from configparser import ConfigParser
import re
from retrievers.langchain_document_loader import load_and_format_logs
from prompts.prompt_templates import apply_prompt_template

# Load configuration
config = ConfigParser()
config.read('../config/elasticsearch_config.json')
slack_config = ConfigParser()
slack_config.read('../config/slack_config.json')

# Initialize Elasticsearch client
es = Elasticsearch([config['elasticsearch']['url']])

# Initialize Pinecone client
pinecone_client = PineconeClient(api_key=config['pinecone']['api_key'], environment=config['pinecone']['environment'])

# Initialize Slack client
slack_client = WebClient(token=slack_config['slack']['token'])

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Analyze the query to determine its type and parameters
def analyze_query(query_text):
    """
    Analyzes the query text to determine if it's structured (date/log level)
    or semantic, and extracts query parameters.
    """
    if "yesterday" in query_text or "last" in query_text:
        # Date-specific query for Elasticsearch
        query_type = "date"
        query_params = {"start_date": "now-1d/d", "end_date": "now"}
    elif "error" in query_text or "warning" in query_text:
        # Log level-specific query for Elasticsearch
        query_type = "level"
        query_params = {"log_level": "ERROR" if "error" in query_text else "WARNING"}
    else:
        # Semantic query for Pinecone
        query_type = "semantic"
        query_params = {"query_text": query_text}
    
    return query_type, query_params

# Process the query using prompt templates and load results from retrievers
def process_query(query_type, query_params):
    """
    Processes the operator query with prompt templates for better accuracy,
    then retrieves and formats logs.
    """
    # Apply a prompt template to the query for optimal search
    formatted_query = apply_prompt_template(query_type, query_params)

    # Load and format logs
    results = load_and_format_logs(query_type, formatted_query)
    return results

# Function to handle Slack messages
def handle_slack_message(event_data):
    query_text = event_data['text']
    user = event_data['user']
    
    # Analyze the query type and parameters
    query_type, query_params = analyze_query(query_text)

    # Process the query with Log Analysis Agent
    results = process_query(query_type, query_params)
    
    # Format response and send to Slack
    response_message = f"Query Results for '{query_text}':\n{json.dumps(results, indent=2)}"
    try:
        slack_client.chat_postMessage(channel=user, text=response_message)
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")

# Placeholder Slack event listener
def slack_event_listener():
    while True:
        # Poll for Slack events here and trigger `handle_slack_message`
        pass

# Main function to process operator query with different retrieval methods
def process_query(query_type, query_params):
    """
    Processes the operator query using Elasticsearch and Pinecone retrievers.
    
    Parameters:
        query_type (str): Type of query ('date', 'level', or 'semantic').
        query_params (dict): Parameters for the query (date range, log level, or query text).
    """
    results = load_and_format_logs(query_type, query_params)
    return results

if __name__ == "__main__":
    slack_event_listener()
