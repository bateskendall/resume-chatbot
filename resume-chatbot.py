import openai
import requests
import json
import os

openai.api_key = os.environ.get("AI_API_KEY")

def call_openai_api(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=500
    )
    return response.choices[0].text.strip()

# Read the initial prompt from a file
with open('resume_info.txt', 'r') as file:
    conversation_history = file.read()

while True:
    user_input = input("User: ")
    conversation_history += "\nUser: " + user_input
    conversation_history += "\nAI: "
    
    ai_response = call_openai_api(conversation_history)
    print("AI: " + ai_response)

    conversation_history += ai_response
