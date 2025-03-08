import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Get detected languages and security-sensitive files from environment variables
detected_languages = os.getenv("DETECTED_LANGUAGES", "").split(", ")
security_files = os.getenv("SECURITY_FILES", "").split(", ")

# Loop through each chunk
for i in range(len(chunks)):
    with open(f"chunk_{i}.txt", "r") as file:
        chunk = file.read()

    # Customize prompt based on detected language
    if "Python" in detected_languages:
        system_prompt = "You are a Python code reviewer. Analyze the following PR diff and provide feedback in a clear, structured format:"
    elif "JavaScript" in detected_languages:
        system_prompt = "You are a JavaScript code reviewer. Analyze the following PR diff and provide feedback in a clear, structured format:"
    else:
        system_prompt = "You are a code reviewer. Analyze the following PR diff and provide feedback in a clear, structured format:"

    # Add a warning if security-sensitive files are touched
    if security_files:
        system_prompt += "\n\n**WARNING:** This PR touches security-sensitive files: " + ", ".join(security_files)

    # Send the chunk to OpenAI for analysis
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": chunk}
        ]
    )

    # Format the feedback
    feedback = response["choices"][0]["message"]["content"]
    formatted_feedback = f"""
    ### Code Review Feedback

    **Summary:**
    {feedback.split('.')[0]}.

    **Detailed Feedback:**
    - {feedback.replace('. ', '.\n- ')}
    """

    print(formatted_feedback)
