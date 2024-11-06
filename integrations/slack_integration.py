from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from configparser import ConfigParser

# Load Slack token
slack_config = ConfigParser()
slack_config.read('../config/slack_config.json')
slack_client = WebClient(token=slack_config['slack']['token'])

def send_slack_message(channel, text):
    try:
        response = slack_client.chat_postMessage(channel=channel, text=text)
        return response
    except SlackApiError as e:
        print(f"Slack error: {e.response['error']}")
