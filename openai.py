from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


prompt=ChatPromptTemplate.from_messages([
    ("system", "you are a helful assistant. Please respond to a user query as per the instructions given."),
    ("user", "Question:{question}")
])

st.title("Simple Chatbot with Langchain and Streamlit")
input_text=st.text_input("Enter your question here:")

llm=ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.7)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))