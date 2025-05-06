import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq()

# Streamlit app
st.title("Groq Chat Assistant")

# Input from the user
user_input = st.text_area("Enter your message:", placeholder="Type your message here...")

# Button to trigger the API call
if st.button("Get Response"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            try:
                # Call the Groq API
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input},
                    ],
                    model="llama-3.3-70b-versatile"
                )
                # Display the response
                response = chat_completion.choices[0].message.content
                st.success("Response:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before clicking the button.")