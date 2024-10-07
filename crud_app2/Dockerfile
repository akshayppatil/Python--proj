# Dockerfile

# Base image: Python 3.10 (you can adjust the version as needed)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port Flask runs on (default is 5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "run.py"]
