import os
import streamlit as st
from quiz_generator import QuizGenerator
from GoogleIt import text_processor 

st.title("Quiz Generator")


def user_response_handler(user_txt):
    """
    Handles the user's input and generates AI response.

    Parameters:
    - user_txt (str): The user's input text.

    Returns:
    None
    """
    st.chat_message("user").markdown(user_txt)

    st.session_state.quiz.append({
        "role": "user", 
        "content": user_txt
    })

    with st.chat_message("ai"):
        with st.spinner("Loading..."):
            response = st.session_state.quiz_model.get_response(user_txt)
            st.markdown(response)

    st.session_state.quiz.append({
        "role": "ai", 
        "content": response
    })


def start_chat():
    """
    Initiates the chat interface and handles user interactions.

    Returns:
    None
    """
    for message in st.session_state.quiz:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Type your message here:")

    if user_input:
        user_response_handler(user_input)


def start_app():
    """
    Starts the Streamlit application and handles the overall flow.

    Returns:
    None
    """
    if "quiz" not in st.session_state:
        st.session_state.quiz = []

        st.session_state.quiz_model = QuizGenerator()

        response = st.session_state.quiz_model.get_initial_response(st.session_state.content)
        
        st.session_state.quiz.append({
            "role": "ai", 
            "content": response
        })
        
        start_chat()
    else:
        start_chat()

def upload_content():
    """
    Handles the upload of a PDF document and initializes the application.

    Returns:
    None
    """
    if "content" not in st.session_state:

        placeholder = st.empty()
        file = placeholder.file_uploader("Upload document", type=["pdf"])

        if file:
            with open("uploadedfile.pdf", "wb") as f:
                f.write(file.read())

            content, _ = text_processor.extract_text_from_pdf(pdf_path="uploadedfile.pdf")

            os.remove("converted_document.docx")
            os.remove("uploadedfile.pdf")

            st.session_state.content = content
            placeholder.empty()

        if "content" in st.session_state:
            start_app()
    else:
        start_app()

if __name__ == "__main__":
    upload_content()