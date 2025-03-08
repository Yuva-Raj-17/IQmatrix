import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get detected languages from environment variable
detected_languages = os.getenv("DETECTED_LANGUAGES", "").split(", ")

# Loop through each chunk
for i in range(len(chunks)):
    with open(f"chunk_{i}.txt", "r") as file:
        chunk = file.read()

    # Customize prompt based on detected language
    if "Python" in detected_languages:
        system_prompt = "You are a Python code reviewer. Analyze the following PR diff:"
    elif "JavaScript" in detected_languages:
        system_prompt = "You are a JavaScript code reviewer. Analyze the following PR diff:"
    elif "PHP" in detected_languages:
        system_prompt = "You are a PHP code reviewer. Analyze the following PR diff:"
    else:
        system_prompt = "You are a code reviewer. Analyze the following PR diff:"

    # Send the chunk to OpenAI for analysis
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": chunk}
        ]
    )
    print(response["choices"][0]["message"]["content"])
