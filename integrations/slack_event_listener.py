import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from configparser import ConfigParser
from agents.log_analysis_agent import process_query
from agents.log_analysis_agent import analyze_query, process_query



# Load Slack configuration
slack_config = ConfigParser()
slack_config.read('../config/slack_config.json')
slack_client = WebClient(token=slack_config['slack']['token'])

def handle_slack_message(event_data):
    query_text = event_data['text']
    user_id = event_data['user']
    
    # Analyze the query type and parameters with memory consideration
    query_type, query_params = analyze_query(query_text, user_id)

    # Process the query and retrieve RAG-based suggestions
    response = process_query(query_type, query_params, user_id)
    
    # Send the results and suggestions back to Slack
    response_message = f"Query Results for '{query_text}':\n\n"
    response_message += f"Results:\n{json.dumps(response['results'], indent=2)}\n\n"
    response_message += f"Contextual Suggestions:\n{json.dumps(response['contextual_suggestions'], indent=2)}"
    
    send_slack_response(user_id, response_message)

def send_slack_response(channel, text):
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")

def slack_event_listener():
    # Placeholder for actual Slack events ingestion
    while True:
        # Listen for events from Slack and trigger `handle_slack_message`
        pass

def handle_slack_message(event_data):
    query_text = event_data.get('text', '')
    user = event_data.get('user', '')

    # Analyze the query type and parameters
    query_type, query_params = analyze_query(query_text)

    # Process the query with Log Analysis Agent
    results = process_query(query_type, query_params)

    # Send the results back to Slack
    response_message = f"Results for '{query_text}':\n{json.dumps(results, indent=2)}"
    send_slack_response(user, response_message)