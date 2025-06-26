import os
import json
import requests
import sys

# Load your API key from the environment variable.
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    sys.exit(1)

# This makes the script interactive.
user_prompt = input("What would you like to ask Gemini? ")

if not user_prompt:
    print("No prompt entered. Exiting.")
    sys.exit()


# The Gemini API URL for the gemini-1.5-flash model
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

# The data we are sending in our POST request.
# The 'text' part uses the variable from our user input.
payload = {
    "contents": [{
        "parts":[{
            "text": user_prompt
        }]
    }]
}

# The headers tell the API that we're sending JSON data.
headers = {
    'Content-Type': 'application/json'
}

print("\nSending your prompt to the Gemini API...")

try:
    # Make the actual POST request
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    # Print the Response 
    response_data = response.json()
    
    # Extract the useful text part of the response
    # Added error handling in case the response format is unexpected
    try:
        text_response = response_data['candidates'][0]['content']['parts'][0]['text']
    except (KeyError, IndexError):
        print("\n--- Could not parse the response ---")
        print("Full Response:")
        print(json.dumps(response_data, indent=2))
        sys.exit(1)

    print("\n--- Gemini's Response ---")
    print(text_response)


except requests.exceptions.HTTPError as err:
    print(f"\nAn HTTP error occurred: {err}")
    print("Response Body:", err.response.text)
except requests.exceptions.RequestException as e:
    print(f"\nA network error occurred: {e}")

