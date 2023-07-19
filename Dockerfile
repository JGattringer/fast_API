FROM ubuntu:latest
LABEL authors="joaog"

ENTRYPOINT ["top", "-b"]

# Use the official Python base image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose the port on which the API will run
EXPOSE 8000

# Run the API using Uvicorn
CMD ["uvicorn", "my_API:app", "--host", "0.0.0.0", "--port", "8000"]
