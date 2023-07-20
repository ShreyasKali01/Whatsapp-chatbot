# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire application to the container
COPY . .

# Expose the port on which your Flask app runs (e.g., 5000)
EXPOSE 5000

# Set the environment variables for the API keys (update these with your actual keys)
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV TWILIO_ACCOUNT_SID=${TWILIO_ACCOUNT_SID}
ENV TWILIO_AUTH_TOKEN=${TWILIO_AUTH_TOKEN}

# Set the environment variable to run the Flask app
ENV FLASK_APP=chatbot.py

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]


