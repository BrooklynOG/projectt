import streamlit as st
from intent import detect_intent
from tasks import add_expense, add_income, get_summary
from rag import load_data, query_data
from llm import generate_response

# Load RAG once
load_data()

st.set_page_config(page_title="Finance Chatbot", layout="wide")

# --- CSS ---
st.markdown("""
<style>
.chat-user {background:#1f77b4;padding:10px;border-radius:10px;margin:5px;text-align:right;}
.chat-bot {background:#262730;padding:10px;border-radius:10px;margin:5px;}
.metric-box {background:#1c1f26;padding:15px;border-radius:12px;text-align:center;}
</style>
""", unsafe_allow_html=True)

if "chat" not in st.session_state:
    st.session_state.chat = []

# --- SIDEBAR ---
st.sidebar.title("⚙️ Controls")

exp = st.sidebar.number_input("Expense ₹", min_value=0)
if st.sidebar.button("Add Expense"):
    st.sidebar.success(add_expense(exp))

inc = st.sidebar.number_input("Income ₹", min_value=0)
if st.sidebar.button("Add Income"):
    st.sidebar.success(add_income(inc))

if st.sidebar.button("Clear Chat"):
    st.session_state.chat = []

# --- TITLE ---
st.title("💰 AI Finance Chatbot")

# --- METRICS ---
data = get_summary()
c1, c2, c3 = st.columns(3)

c1.markdown(f"<div class='metric-box'>💰 Income<br><h2>₹{data['income']}</h2></div>", unsafe_allow_html=True)
c2.markdown(f"<div class='metric-box'>💸 Expense<br><h2>₹{data['expense']}</h2></div>", unsafe_allow_html=True)
c3.markdown(f"<div class='metric-box'>📈 Balance<br><h2>₹{data['balance']}</h2></div>", unsafe_allow_html=True)

st.divider()

# --- CHAT ---
query = st.text_input("Ask something...")

if st.button("Send"):
    intent = detect_intent(query)

    if intent == "expense":
        try:
            amount = int(query.split()[-1])
            response = add_expense(amount)
        except:
            response = "Use: add expense 500"

    elif intent == "income":
        try:
            amount = int(query.split()[-1])
            response = add_income(amount)
        except:
            response = "Use: add income 2000"

    else:
        context = query_data(query)
        prompt = f"Context:\n{context}\n\nQuestion: {query}"
        response = generate_response(prompt)

    st.session_state.chat.append(("user", query))
    st.session_state.chat.append(("bot", response))

# --- DISPLAY ---
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"<div class='chat-user'>👤 {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bot'>🤖 {msg}</div>", unsafe_allow_html=True)
