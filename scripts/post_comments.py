import requests
import os

# Get the formatted feedback from the environment variable
formatted_feedback = os.getenv("FORMATTED_FEEDBACK")

# Post the feedback as a comment on the PR
response = requests.post(
    f"https://api.github.com/repos/{os.getenv('GITHUB_REPOSITORY')}/issues/{os.getenv('PR_NUMBER')}/comments",
    headers={"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"},
    json={"body": formatted_feedback}
)

if response.status_code == 201:
    print("Feedback posted successfully!")
else:
    print(f"Failed to post feedback. Status code: {response.status_code}")
