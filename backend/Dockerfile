# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed dependencies specified in requirements.txt
# RUN pip install --no-cache-dir fastapi uvicorn joblib pandas scikit-learn

# # Expose the port number that the FastAPI app runs on
# EXPOSE 8000

# # Command to run the FastAPI application using uvicorn
# CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]


# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir fastapi uvicorn joblib pandas scikit-learn

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the FastAPI application within the container
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
