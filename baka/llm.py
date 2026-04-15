import requests
import os

API_KEY = os.getenv("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")

def generate_response(prompt):
    if not API_KEY:
        return "API key missing. Set XAI_API_KEY."

    url = "https://api.x.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "grok-1",
        "messages": [
            {"role": "system", "content": "You are a helpful finance assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(url, headers=headers, json=data, timeout=30)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"