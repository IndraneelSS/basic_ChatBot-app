import streamlit as st

# Set up the Streamlit chat interface
st.title(" Neel-Chatbot")

# Display chat messages from the user and the bot
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("bot").write(message["content"])

# Get user input
if user_input := st.chat_input("Say something..."):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Bot response
    bot_response = f"Thank you for telling me {user_input}"
    st.session_state.messages.append({"role": "bot", "content": bot_response})

    # Display bot message
    st.chat_message("bot").write(bot_response)
