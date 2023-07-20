from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import os
from langchain.agents import create_csv_agent
from langchain.agents.agent_types import AgentType


# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

# Load the DataFrame from CSV
pd_agent = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    "leads_test.csv",
    verbose=False,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)
start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''
openai_api_key = os.environ.get('OPENAI_API_KEY')


# Ask the chatbot
def ask(query, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return pd_agent.run(query)

# Define the function to append interaction to chat log
def append_interaction_to_chat_log(query, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log

# Twilio configurations
account_sid = os.environ.get('ACCOUNT_SID')                                             # Twilio Account SID
auth_token = os.environ.get('AUTH_TKN')                                                    # Twilio Account Auth Token
client = Client(account_sid, auth_token)

def sendMessage(body_mess, phone_number):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=body_mess,
        to='whatsapp:' + phone_number
    )

@app.route('/', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    phone_number = request.values['WaId']

    if incoming_msg:
        chat_log = session.get('chat_log')
        answer = ask(incoming_msg, chat_log)
        session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)
        sendMessage(answer, phone_number)

    else:
        sendMessage("Message Cannot Be Empty!")

    r = MessagingResponse()
    r.message("")        
    return str(r)

   
if __name__ == '__main__':
    app.run()

