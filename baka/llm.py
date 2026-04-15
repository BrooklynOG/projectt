import requests
import streamlit as st

# Ensure you have added GROQ_API_KEY in your Streamlit Cloud Secrets
API_KEY = st.secrets["GROQ_API_KEY"]

def generate_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        # Swapped decommissioned 'llama3-70b-8192' for the newer 'llama-3.3-70b-versatile'
        "model": "llama-3.3-70b-versatile",
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

        if "choices" in response_json:
            return response_json["choices"][0]["message"]["content"]
        else:
            return f"Unexpected response: {response_json}"

    except requests.exceptions.HTTPError:
        return f"API Error: {res.text}"
    except Exception as e:
        return f"Error: {str(e)}"
