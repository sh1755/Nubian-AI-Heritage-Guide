import ollama

def load_documents():

    files = [
        "data/nubian_history.txt",
        "data/oral_history.txt"
    ]

    documents = []

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            documents.append(f.read())

    return "\n\n".join(documents)


def ask_question(question):

    knowledge = load_documents()

    prompt = f"""
You are a Nubian heritage guide.

Use ONLY the information below.

Knowledge:

{knowledge}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]