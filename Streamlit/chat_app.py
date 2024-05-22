import streamlit as st
import time
import pandas as pd

# Initialize session state for chat history if not already done
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title('Python Chat App with Streamlit')

# Tab selection
tab = st.radio("Select Mode", ["Chat", "File Upload", "Dataframe", "Options"])

if tab == "Chat":
    # User input section
    user_input = st.text_input("You: ", "")

    # Function to process user input
    def process_input(user_input):
        if user_input:
            response = f"Echo: {user_input}"  # Simple echo response for now
            st.session_state.messages.append({"user": "You", "text": user_input})
            st.session_state.messages.append({"user": "Bot", "text": response})

    # Process input when user presses Enter
    if user_input:
        process_input(user_input)

    # Display chat history
    st.subheader("Chat History")
    for message in st.session_state.messages:
        if message['user'] == "You":
            st.write(f"**{message['user']}:** {message['text']}")
        else:
            st.write(f"*{message['user']}:* {message['text']}")

elif tab == "File Upload":
    # File upload section
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "pptx", "txt"])

    if uploaded_file is not None:
        st.write(f"Uploaded file: {uploaded_file.name}")

elif tab == "Dataframe":
    # Additional UI elements
    if st.checkbox('Show dataframe'):
        data = pd.DataFrame({
            'Column 1': [1, 2, 3, 4],
            'Column 2': [10, 20, 30, 40]
        })
        st.write(data)

elif tab == "Options":
    option = st.selectbox(
        'Select an option',
        ('Option 1', 'Option 2', 'Option 3')
    )

    st.write('You selected:', option)

    # Slider example
    slider_value = st.slider('Select a value', 0, 100, 50)
    st.write('Slider value:', slider_value)

    # Button to run a Python process
    if st.button('Run Python Process'):
        st.write('Running a Python process...')
        time.sleep(2)
        st.write('Process completed.')
