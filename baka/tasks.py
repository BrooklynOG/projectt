import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE = os.path.join(BASE_DIR, "data", "transactions.json")

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(amount):
    data = load_data()
    data.append({"type": "expense", "amount": amount})
    save_data(data)
    return f"Expense added: ₹{amount}"

def add_income(amount):
    data = load_data()
    data.append({"type": "income", "amount": amount})
    save_data(data)
    return f"Income added: ₹{amount}"

def get_summary():
    data = load_data()

    income = sum(d["amount"] for d in data if d["type"] == "income")
    expense = sum(d["amount"] for d in data if d["type"] == "expense")

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }
