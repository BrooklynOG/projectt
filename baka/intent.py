import json
import os

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "data", "intents.json")

with open(file_path) as f:
    intents = json.load(f)

def detect_intent(query):
    query = query.lower()

    for intent, patterns in intents.items():
        for p in patterns:
            if p in query:
                return intent

    return "general"
