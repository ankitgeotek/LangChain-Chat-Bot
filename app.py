# QnA ChatBot
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
from constant import openai_key_2
os.environ['OPENAI_API_KEY']= openai_key_2

load_dotenv()   #take environment variable from .env
import streamlit as st
st.set_page_config(page_title="QnA")
st.title("LangChain Chatbot Application")

def get_openai_response(question):
    llm = OpenAI(openai_api_key= os.environ["OPENAI_API_KEY"], model_name= 'gpt-3.5-turbo-instruct', temperature = 0.6)
    response = llm(question)
    return response


#initialize Streamlit App




input = st.text_input("Input: ", key="input")
response= get_openai_response(input)



but_Submit = st.button("Ask the question")

if but_Submit:
    st.subheader("The Response is")
    st.write(response)









