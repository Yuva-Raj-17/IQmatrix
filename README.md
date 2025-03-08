Step 1:Set Up the Workflow:

Created a GitHub Actions workflow to review PRs automatically.

Added steps to check code, detect languages, and post feedback.

Step 2:Handled Large PRs:

Split big PRs into smaller parts to avoid OpenAI token limits.

Step 3:Detected Programming Languages:

Auto-detected if the PR is for Python, JavaScript, PHP, etc.

Customized the review feedback based on the language.

Step 4:Added Security Checks:

Detected if the PR touches security-sensitive files (like .env or auth/).

Highlighted these files in the review comments.

Step 5:Improved Review Formatting:

Made the review comments clear and easy to read with headings and bullet points.

Step 6:Tested the Workflow:

Tested with sample PRs and real production code.

Verified that the workflow runs smoothly and posts correct feedback.

Step 7:Added Notifications:

Set up Slack or email notifications for workflow results.

How to Use

Set Up Secrets:

Add your OPENAI_API_KEY and other secrets (like Slack webhook or Mailgun API key) in GitHub Secrets.

Create a PR:

Push your code changes and create a pull request.

The workflow will automatically run and post review comments.

Customize:

You can modify the workflow to add more languages, improve feedback, or change notification settings.


Secrets Needed

OPENAI_API_KEY: Your OpenAI API key.

SLACK_WEBHOOK_URL (optional): For Slack notifications.

MAILGUN_API_KEY (optional): For email notifications.
