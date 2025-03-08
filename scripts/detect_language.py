import os

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
    for file in files:
        _, ext = os.path.splitext(file)
        if ext in language_map:
            detected_languages.add(language_map[ext])

    return detected_languages

# Example usage
if __name__ == "__main__":
    # Get list of changed files from environment variable
    changed_files = os.getenv("CHANGED_FILES", "").split()
    languages = detect_language(changed_files)
    print("Detected languages:", ", ".join(languages))
