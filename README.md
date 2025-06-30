# Gemini AI Chat and History Project

## Overview

This project is a Python command-line application that interacts with the Google Gemini API. It allows a user to perform two main actions:
1.  Fetch and display a list of all available Gemini models using a `GET` request.
2.  Ask a question to the Gemini AI using a `POST` request.
3.  Save the entire conversation history (prompts and responses) into a local SQLite database for persistence.

This demonstrates fundamental skills in API interaction, data persistence with databases, and secure credential management.

## Setup Instructions

To run this project, you will need to set up your environment correctly.

### 1. Install Libraries
This project requires three external Python libraries. You can install them using pip:
```bash
pip3 install requests pandas sqlalchemy
```
### 2. Set Environment Variable
This project uses a secure method to handle the API key. You must have your Google Gemini API key set as an environment variable.

On Mac/Linux (in ~/.zshrc or ~/.bashrc):
```bash
export GEMINI_API_KEY='YOUR_API_KEY_HERE'
```
Remember to restart your terminal or run source ~/.zshrc after adding the key.

### How to Run Your Code
Once the setup is complete, you can run the application with the following command (assuming your file is named gemini_project.py):
```bash
python3 gemini_project.py
```
The script will then prompt you with two choices:

Enter list to see the available Gemini models.

Press Enter to be prompted to ask a question.

### Overview of How the Code Works
The script is organized into functions for clarity:

list_available_models(): This function makes a GET request to the /models endpoint of the Gemini API. It then parses the JSON response and prints a clean list of all models that support content generation.

generate_content(prompt): This function takes a user's prompt, formats it into a JSON payload, and sends it to the Gemini API via a POST request. After receiving the response, it does two things:

Parses the JSON to extract and print the model's text answer.

Uses pandas and sqlalchemy to save the prompt and the response into a SQLite database file named gemini_history.db. If the table or database doesn't exist, they are created automatically.

The main (if __name__ == "__main__":) block handles the initial user interaction, asking the user what action they want to perform and calling the appropriate function.