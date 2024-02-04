import os
from dotenv import load_dotenv
import google.generativeai as genai
from utility import PROMPT

load_dotenv()

# Load Google API key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


class QuizGenerator:
    """
    A class representing a Quiz Generator using Google Gemini chat model.

    Attributes:
    - history (list[dict[str, str]]): A list to store the history of user and AI interactions.
    - chat (GenerativeChat): An instance of the GenerativeChat class for chat interactions.

    Methods:
    - get_initial_response(content: str) -> str: Gets the initial AI response based on the provided content.
    - get_response(user_input: str) -> str: Gets the AI response based on the user's input.
    """

    def __init__(self) -> None:
        """
        Initializes the QuizGenerator class.

        Creates a chat instance using the Google Gemini GenerativeModel.
        """
        self.history: list[dict[str, str]] = []

        # Initialize the GenerativeModel with 'gemini-pro'
        model = genai.GenerativeModel('gemini-pro')

        # Start a chat with an empty history
        self.chat = model.start_chat(history=[])

    def get_initial_response(self, content: str) -> str:
        """
        Gets the initial AI response based on the provided content.

        Parameters:
        - content (str): The initial content for generating the AI response.

        Returns:
        str: The AI-generated response.
        """
        response = self.chat.send_message([content, PROMPT])
        return response.text

    def get_response(self, user_input: str) -> str:
        """
        Gets the AI response based on the user's input.

        Parameters:
        - user_input (str): The user's input text.

        Returns:
        str: The AI-generated response.
        """
        current = {"user": user_input}

        response = self.chat.send_message(user_input)

        current["ai"] = response.text

        self.history.append(current)

        return response.text.replace("\n", "\n\n")
