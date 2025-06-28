import os
import json
import requests
import sys
import pandas as pd
import sqlalchemy as db

# Load your API key from the environment variable.
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    sys.exit(1)

# Function for the GET Request 
def list_available_models():
    """
    Makes a GET request to the Gemini API to list all available models
    and prints them in a readable format.
    """
    print("\nFetching available models...")
    
    # The URL for the models endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for any errors
        
        models_data = response.json()
        
        print("\n--- Available Gemini Models ---")
        # Parse the JSON to print something useful
        for model in models_data.get('models', []):
            # We only want to show models that support generating content
            if 'generateContent' in model.get('supportedGenerationMethods', []):
                print(f"- {model['displayName']} ({model['name']})")

    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")


# Function for the POST Request 
def generate_content(prompt):
    """
    Makes a POST request to the Gemini API to generate content based on a prompt.
    """
    print("\nSending your prompt to the Gemini API...")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
    payload = {"contents": [{"parts":[{"text": prompt}]}]}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
        
        text_response = response_data['candidates'][0]['content']['parts'][0]['text']
        
        print("\n--- Gemini's Response ---")
        print(text_response)

        
        # 1. Convert your dictionary into a pandas dataframe.
        #    We'll create a dictionary to hold our prompt and the response.
        conversation_data = {
            'prompt': [prompt],
            'response': [text_response]
        }
        df = pd.DataFrame.from_dict(conversation_data)

        # 2. Import sqlalchemy (already done at the top)

        # 3. Create an engine object.
        #    This creates a file named 'gemini_history.db' in your project folder.
        engine = db.create_engine('sqlite:///gemini_history.db')

        # 4. Create and send SQLTable from your dataframe.
        #    - 'conversation_log' is the name of our table inside the database.
        #    - if_exists='append' will add new data to the table. If the table
        #      doesn't exist, it will be created. This is perfect for a chat log.
        df.to_sql('conversation_log', con=engine, if_exists='append', index=False)
        print("\n...Conversation saved to database.")

        # 5. Write a query and print out the results.
        #    This proves our data was saved correctly by reading it all back.
        with engine.connect() as connection:
            # We select all rows from our table
            query = "SELECT * FROM conversation_log"
            query_result = connection.execute(db.text(query)).fetchall()
            
            # Use pandas again to display the results in a nice format.
            history_df = pd.DataFrame(query_result)
            print("\n--- Full Conversation History from Database ---")
            print(history_df)

    except requests.exceptions.HTTPError as err:
        print(f"\nAn HTTP error occurred: {err}")
    except (KeyError, IndexError):
        print("\n--- Could not parse the API response ---")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


# Main execution block
if __name__ == "__main__":
    # Give the user a choice of what action to perform
    choice = input("Enter 'list' to see available models, or press Enter to ask a question: ").lower()
    
    if choice == 'list':
        list_available_models()
    else:
        user_prompt = input("What would you like to ask Gemini? ")
        if user_prompt:
            generate_content(user_prompt)
        else:
            print("No prompt entered. Exiting.")
