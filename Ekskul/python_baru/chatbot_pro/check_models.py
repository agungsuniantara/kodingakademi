import streamlit as st
from groq import Groq
import os

# Ensure secrets are loaded or handle error
try:
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
    else:
        # Fallback for running directly not via streamlit if needed
        import toml
        with open(".streamlit/secrets.toml", "r") as f:
            secrets = toml.load(f)
            api_key = secrets.get("GROQ_API_KEY")
except Exception as e:
    print(f"Error loading secrets: {e}")
    exit(1)

client = Groq(
    api_key=api_key
)

try:
    print(f"Fetching models from Groq...")
    models = client.models.list()
    
    print("\n--- AVAILABLE MODELS ---")
    for model in models.data:
        print(f"- {model.id}")
        
except Exception as e:
    print(f"Error fetching models: {e}")
