import json
from datetime import datetime, timedelta

# Memory structure to store recent conversations, keyed by user ID
class MemoryModule:
    def __init__(self):
        # Dictionary to hold memory; each user has a list of recent conversations
        self.memory_store = {}

    def add_to_memory(self, user_id, query, response):
        """
        Adds a query and response to the user's memory.

        Parameters:
            user_id (str): Unique identifier for the user.
            query (str): The query from the user.
            response (str): The response given by the agent.
        """
        # Initialize memory for the user if not present
        if user_id not in self.memory_store:
            self.memory_store[user_id] = []

        # Store conversation with a timestamp
        conversation = {
            "timestamp": datetime.now(),
            "query": query,
            "response": response
        }
        self.memory_store[user_id].append(conversation)

    def retrieve_memory(self, user_id):
        """
        Retrieves recent conversations for the user.

        Parameters:
            user_id (str): Unique identifier for the user.

        Returns:
            list: Recent conversations (within the last 5 minutes).
        """
        if user_id not in self.memory_store:
            return []

        # Filter conversations to return only those from the last 5 minutes
        current_time = datetime.now()
        recent_conversations = [
            convo for convo in self.memory_store[user_id]
            if current_time - convo["timestamp"] < timedelta(minutes=5)
        ]

        return recent_conversations

    def clear_old_memory(self, user_id):
        """
        Clears outdated memory entries for a user to maintain relevance.

        Parameters:
            user_id (str): Unique identifier for the user.
        """
        if user_id not in self.memory_store:
            return

        # Only keep conversations from the last 5 minutes
        current_time = datetime.now()
        self.memory_store[user_id] = [
            convo for convo in self.memory_store[user_id]
            if current_time - convo["timestamp"] < timedelta(minutes=5)
        ]
