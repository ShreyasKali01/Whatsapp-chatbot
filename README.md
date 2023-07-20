Documentation for the provided Python Flask application:

# WhatsApp Chatbot using Flask and Twilio

This is a simple WhatsApp chatbot application built using Flask, Twilio, and the OpenAI GPT-3.5 model. The chatbot is designed to interact with users and respond to their queries based on the data available in a CSV file. The OpenAI GPT-3.5 model powers the chatbot, providing natural language understanding and generation capabilities.

## Prerequisites

Before running the application, ensure you have the following:

- Python (3.6 or higher) installed on your system
- Twilio account with a valid WhatsApp-enabled phone number
- OpenAI API key for accessing the GPT-3.5 model
- CSV file containing data for the chatbot to respond to queries

## Installation

1. Clone the repository and navigate to the project directory:

```bash
git clone <repository_url>
cd whatsapp_chatbot
```

2. Install the required Python packages:

```bash
pip install flask twilio pandas langchain
```

## Configuration

1. Set up the environment variables:

   - `ACCOUNT_SID`: Your Twilio account SID
   - `AUTH_TKN`: Your Twilio account auth token
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `FLASK_ENV`: Set it to `production` when deploying to production

   Note: It's recommended to use a `.env` file to store these environment variables securely.

2. Prepare the CSV file:

   Ensure that you have a CSV file named "leads_test.csv" with the necessary data for the chatbot to respond to queries.

## Usage

To run the application, execute the following command:

```bash
python app.py
```

The Flask app will start running, and you should see the server address in the console.

## How the Chatbot Works

The WhatsApp chatbot interacts with users using natural language. When a user sends a message, the Twilio webhook forwards the message to the Flask app, which processes the incoming query.

The Flask app uses the OpenAI GPT-3.5 model to understand and generate responses. The GPT-3.5 model is trained to interpret natural language and can provide appropriate answers based on the given data.

The application uses LangChain, a library for creating interactive chat applications. It leverages OpenAI's GPT-3.5 model for generating responses. The CSV file is read using Pandas to create a DataFrame and is used by the chatbot to respond to user queries.

When the chatbot generates a response, it sends the response back to the user's WhatsApp number using Twilio.

## Interacting with the Chatbot

1. Send a message to the WhatsApp number associated with your Twilio account.
2. The Flask app processes the message and generates a response based on the OpenAI GPT-3.5 model.
3. The response is sent back to your WhatsApp number via Twilio, and you receive the reply.

## Customizing the Chatbot

You can customize the chatbot's behavior by modifying the OpenAI GPT-3.5 model parameters, the CSV file data, and the app's response logic. Additionally, you can integrate other data sources or APIs to enhance the chatbot's capabilities.

## Deployment

To deploy the application to production, ensure you set the `FLASK_ENV` environment variable to `production` to enable production mode in Flask.

You can deploy the application to various platforms like AWS, Google Cloud Platform, or Heroku. For production deployment, consider using WSGI servers like Gunicorn or uWSGI.

Remember to configure your Twilio account for production usage and set the necessary environment variables securely.

## Conclusion

This WhatsApp chatbot demonstrates how to build an interactive and conversational application using Flask, Twilio, and the OpenAI GPT-3.5 model. It can be extended and customized to handle various user queries based on the provided CSV data and the capabilities of the GPT-3.5 model.

Please ensure that you comply with Twilio's terms of service and OpenAI's usage policies while using the respective APIs and services in your application.
