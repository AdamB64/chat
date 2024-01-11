from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv('OPENAI_API_KEY')

from openai import OpenAI

client = OpenAI(
    api_key=api_key
)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "you know most things about programming"},
    {"role": "user", "content": input("talk to chatGTP: ")}
  ]
)

print(completion.choices[0].message)