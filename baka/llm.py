import requests
import streamlit as st

API_KEY = st.secrets["GROQ_API_KEY"]

def generate_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful finance assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        res.raise_for_status()

        response_json = res.json()

        # SAFE extraction
        if "choices" in response_json:
            return response_json["choices"][0]["message"]["content"]
        else:
            return f"Unexpected response: {response_json}"

    except requests.exceptions.HTTPError as e:
        return f"API Error: {res.text}"

    except Exception as e:
        return f"Error: {str(e)}"
