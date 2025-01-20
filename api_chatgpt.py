# File: /Python/api_chatgpt.py

# pip install openai
from openai import OpenAI

# Set your API key:
client = OpenAI(api_key='your_key')

# Generate your API Key:
# https://platform.openai.com/settings/organization/api-keys

# Set your API key:

# How to make an API call:
# https://platform.openai.com/docs/api-reference/streaming

# System persona definition and message history:
my_messages = [
    {"role": "system", "content": "You are an excellent assistant!"}
]

input_message = input('Ask your question: ')
my_messages.append(
    {"role": "user", "content": input_message}
)

# Loop while there is no 'end':
while input_message != 'end':
    response = client.chat.completions.create(model = 'gpt-3.5-turbo',
    messages = my_messages,
    temperature = 1,
    max_tokens = 200)
    answer = response.choices[0].messages.content
    my_messages.append(
        {"role": "assistant", "content": answer}
    )

    # Print answer:
    print('Answer:', answer)
    input_message = input('Ask your question: ')
my_messages.append(
    {"role": "user", "content": input_message}
)
