import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv
import pandas as pd
from langchain.llms import OpenAI
from pandasai import PandasAI
load_dotenv()

# Set the title of your Streamlit app
st.title("PandasAI Chatbot")
# Access OpenAI API key from environment variables
openai_api_key = os.environ.get("apikey")
# Check if the environment variables are loaded correctly
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the .env file.")
llm = OpenAI(api_token=openai_api_key)
pandas_ai = PandasAI(llm, save_charts=True, save_charts_path="//Users//_uh17//Downloads//deploy_powerbi//powerBI")

# Streamlit app title
st.title("PandasAI Streamlit App")
df = pd.read_excel(r"//Users//_uh17//Downloads//deploy_powerbi//phones_data.xlsx")

# Display the Iris dataset
st.subheader("Sample Dataset")
st.write(df)

# Initialize conversation history
conversation = []

# User input for PandasAI prompts
user_input = st.text_input("You: Ask a question or provide a prompt:")

if user_input:
    # Add user input to the conversation
    conversation.append({"role": "user", "message": user_input})

    # Running PandasAI prompt
    response = pandas_ai.run(df, user_input)

    if user_input != None and response == None:
        user_input = user_input + " and save image as plot.png"
        conversation.append({"role": "user", "message": user_input})
        response = pandas_ai.run(df, user_input)
        image = Image.open("/Users/_uh17/Downloads/deploy_powerbi/plot.png")

        # Display the specified PNG image
        st.image(image, caption="Specified PNG Image", use_column_width=True)
    else:
        conversation.append({"role": "pandasai", "message": response})

        # Display text response from PandasAI
        st.subheader("PandasAI Response:")
        st.write(response)

# Save and display conversation history
st.subheader("Conversation History:")
for item in conversation:
    if item["role"] == "user":
        st.text(f"You: {item['message']}")
    elif item["role"] == "pandasai":
        st.text(f"PandasAI: {item['message']}")

st.sidebar.text("Powered by PandasAI and OpenAI")
