import json

with open("data/intents.json") as f:
    intents = json.load(f)

def detect_intent(query):
    query = query.lower()

    for intent, patterns in intents.items():
        for p in patterns:
            if p in query:
                return intent

    return "general"