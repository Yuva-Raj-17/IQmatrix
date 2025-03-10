import os

# Define security-sensitive files
SECURITY_FILES = [".env", "auth/", "secrets/", "config/keys.py"]

def detect_language(files):
    # Map file extensions to languages
    language_map = {
        ".py": "Python",
        ".js": "JavaScript",
        ".php": "PHP",
        ".java": "Java",
        ".go": "Go",
        ".rb": "Ruby",
        ".ts": "TypeScript",
        # Add more extensions as needed
    }

    detected_languages = set()
    security_files_touched = []

    for file in files:
        # Check if the file is security-sensitive
        for pattern in SECURITY_FILES:
            if pattern in file:
                security_files_touched.append(file)

        # Detect language based on file extension
        _, ext = os.path.splitext(file)
        if ext in language_map:
            detected_languages.add(language_map[ext])

    return detected_languages, security_files_touched

# Example usage
if __name__ == "__main__":
    # Get list of changed files from environment variable
    changed_files = os.getenv("CHANGED_FILES", "").split()
    languages, security_files = detect_language(changed_files)
    print("Detected languages:", ", ".join(languages))
    print("Security-sensitive files touched:", ", ".join(security_files))
