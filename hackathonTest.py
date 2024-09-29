import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to get a response from the OpenAI GPT model
def get_chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Correct model name
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app
st.title("AI Chatbot")

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Get response from the chatbot
        bot_response = get_chatbot_response(user_input)
        # Append the user's message and bot's response to session state
        st.session_state.messages.append(f"You: {user_input}")
        st.session_state.messages.append(f"Bot: {bot_response}")
        # Display the bot response in a text area
        st.text_area("Chatbot:", value=bot_response, height=200, max_chars=None, key=None)
    else:
        st.warning("Please enter a message.")

# Display the conversation history
for message in st.session_state.messages:
    st.write(message)
