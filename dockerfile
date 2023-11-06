# Use an official Python runtime as a parent image
FROM python:3.8.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . .

# Expose the port that the Streamlit app will run on
EXPOSE 8501

# Run the Streamlit app when the container launches
CMD ["streamlit", "run", "pandasai_app.py"]
