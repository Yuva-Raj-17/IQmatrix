import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

for i in range(len(chunks)):
    with open(f"chunk_{i}.txt", "r") as file:
        chunk = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code reviewer. Analyze the following PR diff:"},
            {"role": "user", "content": chunk}
        ]
    )
    print(response["choices"][0]["message"]["content"])
