import os
import json
import requests
import sys

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

    except requests.exceptions.HTTPError as err:
        print(f"\nAn HTTP error occurred: {err}")
        print("Response Body:", err.response.text)
    except (KeyError, IndexError):
        print("\n--- Could not parse the response ---")
        print("Full Response:")
        print(json.dumps(response_data, indent=2))


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
