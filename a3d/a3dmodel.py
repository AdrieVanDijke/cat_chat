import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

class A3DModel:
    def __init__(self):
        self.api_openai_key = st.secrets["OPENAI_API_KEY"]
        self.pinecone_api_key = st.secrets["PINECONE_API_KEY"]
        self.pinecone_environment = st.secrets["PINECONE_ENVIRONMENT"]
        self.pinecone_index_name = st.secrets["PINECONE_INDEX_NAME"]
        self.mode = 'Documents'
        self.aimodel = "gpt-3.5-turbo"
        self.engine = "davinci"
        self.api = "OpenAI API"
        self.temperature = 0.0 # chatcompletion / completion parameter
        self.max_tokens = 1200 # chatcompletion / completion parameter
        self.frequency_penalty = 0.0 # completion parameter
        self.presence_penalty = 0.0 # completion parameter
        self.top_p = 0.2 # completion parameter
        self.n_epochs = 4 # training parameter
        self.stop = "" # completion parameter
        
        