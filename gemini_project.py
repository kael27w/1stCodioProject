import os
import json
import requests
import sys
import pandas as pd
import sqlalchemy as db

# --- Helper Functions (for easier testing) ---

def parse_model_response(models_data):
    """
    Parses the raw JSON from the models API and returns a list of model names.
    This function is pure and easily testable.
    """
    model_list = []
    for model in models_data.get('models', []):
        if 'generateContent' in model.get('supportedGenerationMethods', []):
            model_list.append(f"- {model['displayName']} ({model['name']})")
    return model_list

def parse_content_response(response_data):
    """
    Parses the raw JSON from the generateContent API and returns the text response.
    This function is pure and easily testable.
    """
    try:
        return response_data['candidates'][0]['content']['parts'][0]['text']
    except (KeyError, IndexError):
        return None

# --- Main Application Logic ---

API_KEY = os.environ.get("GEMINI_API_KEY")

def list_available_models():
    """Makes a GET request to list available models."""
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    print("\nFetching available models...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        models_data = response.json()
        
        # Use our testable helper function to process the data
        formatted_models = parse_model_response(models_data)
        
        print("\n--- Available Gemini Models ---")
        for model_line in formatted_models:
            print(model_line)

    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")

def generate_content(prompt):
    """Makes a POST request and saves the conversation to a database."""
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    print("\nSending your prompt to the Gemini API...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
    payload = {"contents": [{"parts":[{"text": prompt}]}]}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
        
        # Use our testable helper function to get the text
        text_response = parse_content_response(response_data)
        
        if text_response is None:
            print("\n--- Could not parse the API response ---")
            return

        print("\n--- Gemini's Response ---")
        print(text_response)

        # --- Database Logic ---
        conversation_data = {'prompt': [prompt], 'response': [text_response]}
        df = pd.DataFrame.from_dict(conversation_data)
        engine = db.create_engine('sqlite:///gemini_history.db')
        df.to_sql('conversation_log', con=engine, if_exists='append', index=False)
        print("\n...Conversation saved to database.")

    except requests.exceptions.HTTPError as err:
        print(f"\nAn HTTP error occurred: {err}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    choice = input("Enter 'list' to see available models, or press Enter to ask a question: ").lower()
    
    if choice == 'list':
        list_available_models()
    else:
        user_prompt = input("What would you like to ask Gemini? ")
        if user_prompt:
            generate_content(user_prompt)
        else:
            print("No prompt entered. Exiting.")
