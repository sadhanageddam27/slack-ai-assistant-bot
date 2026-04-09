import os
import requests


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the LLM and returns the response text.
    Uses OpenAI-compatible API by default.
    Swap the base URL to use a local model (e.g., Ollama).
    """

    api_key = os.environ.get("OPENAI_API_KEY", "")
    base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
    model = os.environ.get("LLM_MODEL", "gpt-3.5-turbo")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant integrated into Slack. "
                    "Give clear, concise, and accurate responses. "
                    "Format responses using Slack markdown where helpful."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }

    try:
        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except requests.exceptions.Timeout:
        return ":warning: The request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return ":warning: Could not connect to the LLM service. Check your configuration."

    except Exception as e:
        return f":warning: Something went wrong: {str(e)}"
