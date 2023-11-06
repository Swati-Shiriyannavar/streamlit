from flask import Flask, render_template, send_file, request, flash, redirect, url_for
import pandas as pd
from pandasai import PandasAI
from langchain.llms import OpenAI
from pandasai.llm.openai import OpenAI
import os
import json

app = Flask(__name__)

# Load the LLM configuration from the llm_config.json file
with open("llm_config.json", "r") as config_file:
    llm_config = json.load(config_file)

# Access OpenAI API key and model from the configuration
openai_api_key = llm_config["api_token"]
llm_model = llm_config["model"]

# Create the OpenAI instance
llm = OpenAI(api_token=openai_api_key, model=llm_model)

# Create PandasAI with the LLM
pandas_ai = PandasAI(llm, save_charts=True, save_charts_path="//Users//_uh17//Downloads//flask_api")

# Load the dataset directly (book.csv in this case)
df = pd.read_excel("//Users//_uh17//Downloads//flask_api//phones_data.xlsx")  # Replace with the path to your dataset file

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")

        if user_input:
            response = pandas_ai.run(df, user_input)
            response = pandas_ai.run(df, user_input)
            print(response)


            if user_input and response is None:
                user_input = user_input + " and save image as plot.png"
                response = pandas_ai.run(df, user_input)
                image_path = "//Users//_uh17//Downloads//flask_api//plot.png"
                return send_file(image_path, as_attachment=False)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
