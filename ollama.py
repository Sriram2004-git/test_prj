from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st


prompt=ChatPromptTemplate.from_messages([
    ("system", "you are a helful assistant. Please respond to a user query as per the instructions given."),
    ("user", "Question:{question}")
])

st.title("Simple Chatbot with Langchain and Streamlit")
input_text=st.text_input("Enter your question here:")

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))