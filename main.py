from dotenv import load_dotenv
load_dotenv()
import streamlit as st

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(model="gpt-4o-mini")

st.title('AI POET')

content = st.text_input('Please enter a poem topic.')

if st.button('Create Poem'):
    with st.spinner('Creating your poem...', show_time=True):
        result = chat_model.invoke(f"Write a poem about {content}.")
        st.write(result.content)
