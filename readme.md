# Quiz Generator with Google Gemini Chat Model

## Overview

This Quiz Generator application utilizes the Google Gemini pro chat model to generate quiz questions from a provided PDF file. The application is built using the Streamlit framework.


## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/william-renaldy/quiz-generator.git
cd quiz-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables by creating a `.env` file and adding your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key
```

## Running the Application

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Upload a PDF file containing the content for quiz generation.
2. The application will process the PDF file and display the generated quiz questions.
3. Interact with the chat interface to receive quiz questions and responses.

## File Structure

- **quiz_generator.py:** Contains the QuizGenerator class responsible for interacting with the Google Gemini chat model.
- **app.py:** Streamlit application file for the quiz generator.
- **utility.py** Contains the Prompt template for the model

## Note

- Ensure that you have a valid Google API key to use the Gemini chat model. You can obtain one from the Google Cloud Console.