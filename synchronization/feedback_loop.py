class FeedbackLoop:
    def __init__(self):
        # Stores feedback for analysis
        self.feedback_store = []

    def collect_feedback(self, user_id, query, response, feedback):
        """
        Collects feedback from operators on responses.

        Parameters:
            user_id (str): Unique identifier for the user.
            query (str): The query submitted by the user.
            response (str): The response generated by the agent.
            feedback (str): User feedback on the response (e.g., "useful", "needs improvement").
        """
        feedback_entry = {
            "user_id": user_id,
            "query": query,
            "response": response,
            "feedback": feedback,
            "timestamp": datetime.now()
        }
        self.feedback_store.append(feedback_entry)
        print(f"Feedback collected from user {user_id}: {feedback}")

    def apply_feedback(self):
        """
        Analyzes collected feedback and adjusts prompt templates or retrieval logic.
        """
        for entry in self.feedback_store:
            # Example: If feedback indicates "needs improvement," adjust templates or queries
            if entry["feedback"] == "needs improvement":
                # Logic to adjust prompts or refine retrieval
                print(f"Refining response for query: {entry['query']} based on feedback.")
        
        # Clear feedback after processing
        self.feedback_store = []