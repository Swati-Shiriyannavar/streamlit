import streamlit as st
from pandasai import PandasAI
from langchain.llms import OpenAI
import seaborn as sns
import io
import matplotlib.pyplot as plt
 
# Assigning API key
openaikey = "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"
llm = OpenAI(api_token=openaikey)
 
# Calling PandasAI
pandas_ai = PandasAI(llm)
 
# iris inbuilt dataset from seaborn
iris = sns.load_dataset('Recruitment')
 
# Generate a histogram plot
response = pandas_ai.run(iris, prompt='Plot the histogram of the entries')
 
# Display the generated response
st.title("PandasAI Histogram Plot")
st.write("Response from PandasAI:")
st.write(response)
 
# Plot the histogram and display it using Streamlit
if "plot" in response:
    plt.figure()
    exec(response["plot"])
    st.pyplot()
 
# Optionally, you can also save the plot as an image file
# and display the saved image using Streamlit
if "plot_image" in response:
    image_data = io.BytesIO(response["plot_image"])
    st.image(image_data, use_column_width=True, caption="Generated Plot")
 
st.write("Assistant's response:")
st.write(response["response"])
 