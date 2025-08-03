import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

with open("pytest.log", "r") as f:
    log_content = f.read()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a senior QA engineer. Analyze the pytest log below and summarize any errors or issues that occurred. Suggest possible root causes."
        },
        {
            "role": "user",
            "content": log_content[:3000]  # limit to avoid token overflow
        }
    ]
)

print("GPT Analysis:\n")
print(response.choices[0].message.content)
