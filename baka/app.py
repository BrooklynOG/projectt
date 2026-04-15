import streamlit as st
import requests

st.set_page_config(page_title="Finance Chatbot")

st.title("💰 AI Finance Chatbot")

query = st.text_input("Enter your query")

if st.button("Send"):
    if query.strip():
        try:
            res = requests.post(
                "http://127.0.0.1:8000/chat",
                params={"query": query},
                timeout=10
            )
            st.success(res.json().get("response", "No response"))
        except Exception as e:
            st.error(f"Error: {e}")

st.subheader("📊 Financial Summary")

if st.button("Get Summary"):
    try:
        res = requests.get("http://127.0.0.1:8000/summary")
        data = res.json()

        st.write(f"Income: ₹{data['income']}")
        st.write(f"Expense: ₹{data['expense']}")
        st.write(f"Balance: ₹{data['balance']}")
    except Exception as e:
        st.error(f"Error: {e}")