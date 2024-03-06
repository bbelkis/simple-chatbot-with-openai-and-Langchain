from langchain.llms import OpenAI
import os 
import streamlit as st
from dotenv import load_dotenv
load_dotenv() # env variable with the API KEY

# Load openAI model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name = "gpt-3.5-turbo-instruct", temperature = 0.5)
    response = llm(question)
    return response

# Initialize stramlit app
st.set_page_config(page_title="Q&A app")
st.header("Langchain application")

# Get input text
input = st.text_input("Input: ", key=input)
response = get_openai_response(input)

# Submit button 
submit = st.button("Generate a response")


if submit:
    st.subheader("Answer: ")
    st.write(response)

