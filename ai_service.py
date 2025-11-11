import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OPENAI_API_KEY is expected to be set in environment variables inside your .env file.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    """Use OpenAI to split a complex task into 3-5 simple actionable subtasks."""

    if not client.api_key:
        return ["Error: OpenAI API key is not configured."]
    
    try:
        prompt = f"""Break down the following complex task into a list of 3 to 5 simple, actionable subtasks.

Task: {description}

Response format:
- Subtask 1
- Subtask 2
- Subtask 3
- etc.

Reply only with the list of subtasks, one per line, starting each line with a hyphen."""
        # All parameters are optional except "model" and "messages".
        # See the API docs: https://platform.openai.com/docs/api-reference/chat/create
        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "You are an expert task management assistant that helps break down complex tasks into simple, actionable steps."},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()
        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else ["Error: Could not generate subtasks."]

    except Exception:
        return ["Error: Could not connect to OpenAI."]