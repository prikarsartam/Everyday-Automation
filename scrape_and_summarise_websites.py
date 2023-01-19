# Import libraries
import requests
from bs4 import BeautifulSoup
import openai
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the website URL
# url = "https://www.example.com"

url = str(input("\nEnter the URL: "))

# Retrieve the HTML from the website
html = requests.get(url).text

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Extract the main text from the website
text = soup.get_text()

# Summarize the text using the OpenAI API
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=(f"Summarize the main information from the website {url}"),
  temperature=0.5,
  max_tokens=100,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)

# Print the summary
print(response["choices"][0]["text"])

# Ask a question based on the parsed HTML
question = input("\nWhat do you want to know? ")

# Use the OpenAI API to answer the question
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"Based on the information from the website {url}, {question}",
  temperature=0.5,
  max_tokens=100,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1,
  stop=f"{text}"
)


# Print the answer
print(response["choices"][0]["text"])