# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy both backend and frontend files into the container at /app
COPY . /app

# Install Streamlit and other frontend dependencies
RUN pip install --no-cache-dir streamlit requests

# Expose the port number that Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
