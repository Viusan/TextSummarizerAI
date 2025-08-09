import openai # Automatically reads API key from environment variable
openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}]
)
print(response['choices'][0]['message']['content'])
