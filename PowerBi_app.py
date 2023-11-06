import streamlit as st
import requests
import json
import pandas as pd

# Define your Power BI workspace, dataset, and report details
workspace_id = 'YOUR_WORKSPACE_ID'
dataset_id = 'YOUR_DATASET_ID'
report_id = 'YOUR_REPORT_ID'
access_token = 'YOUR_ACCESS_TOKEN'  # Replace with your access token

# Power BI REST API base URL
api_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}'

# Streamlit app title
st.title("Power BI Q&A Streamlit App")

# User input for the Q&A query
user_query = st.text_input("Ask a question in Power BI Q&A:")

if st.button("Submit Query"):
    if user_query:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        query_data = {
            'query': user_query
        }

        # Send a POST request to Power BI's Q&A API
        response = requests.post(f'{api_url}/datasets/{dataset_id}/tables/main/GenerateToken', headers=headers, data=json.dumps(query_data))

        if response.status_code == 200:
            result = response.json()
            token = result['token']
            embed_url = result['embedUrl']

            st.subheader("Power BI Q&A Response:")
            st.write(f"Query: {user_query}")

            # Display the Q&A response using an embedded Power BI report
            st.components.v1.iframe(embed_url, width=800, height=600)
        else:
            st.error("Error while querying Power BI. Please check your credentials and query.")
    else:
        st.warning("Please enter a query in the input field.")

st.sidebar.text("Powered by Streamlit and Power BI")
