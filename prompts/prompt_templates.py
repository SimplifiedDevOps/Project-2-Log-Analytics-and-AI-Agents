import json

# Load prompt templates from JSON file
with open('../prompts/prompt_templates.json') as f:
    prompt_templates = json.load(f)

def apply_prompt_template(query_type, query_params):
    """
    Applies a prompt template based on query type and fills it with parameters.
    """
    template = prompt_templates.get(query_type)
    return template.format(**query_params) if template else query_params
