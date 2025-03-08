import tiktoken

def split_diff(diff, max_tokens=128000):
    encoding = tiktoken.get_encoding("cl100k_base")  # Encoding for GPT-4
    tokens = encoding.encode(diff)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = tokens[i:i + max_tokens]
        chunks.append(encoding.decode(chunk))
    return chunks

with open("pr_diff.txt", "r") as file:
    diff = file.read()

chunks = split_diff(diff)
for i, chunk in enumerate(chunks):
    with open(f"chunk_{i}.txt", "w") as file:
        file.write(chunk)
