import streamlit as st
from powerbiclient import Report
import requests

# Streamlit UI
st.title("Power BI Q&A Chatbot")

# Search Box
search_query = st.text_input("Ask a question:")

# Button to Generate Q&A Visual
if st.button("Generate"):
    if search_query:
        # Replace with your Power BI embed token and embed URL
        access_token = "YOUR_ACCESS_TOKEN"
        embed_url = "YOUR_EMBED_URL"

        # Construct the Q&A URL with the user's question
        qa_url = f"{embed_url}&sectionIndex=0&qna=AskAQuestion:{search_query}"

        # Embed the Q&A using the Power BI client
        report = Report(qa_url, token=access_token)
        report.init()
        report.render()

    else:
        st.warning("Please enter a question before generating.")

st.markdown("Example Power BI Embed URL: YOUR_EMBED_URL")
