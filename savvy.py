import typer
import chromadb
import ollama


DB_PATH = "db"
COLLECTION_NAME = "git_knowledge"
LLM_MODEL = "llama3:8b"

app = typer.Typer()

@app.command()
def main(
    user_query: str = typer.Argument(..., help="The incorrect git command you want to fix.")
):
   
    print("🤔 Analyzing your command...")

    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)

    results = collection.query(
        query_texts=[user_query],
        n_results=3
    )
    
    retrieved_docs = results['documents'][0]
    context = "\n".join([f"- {doc}" for doc in retrieved_docs])

    prompt = f"""
    You are an expert Git assistant. A user has entered an incorrect command.
    Based on their input and the following relevant documentation snippets,
    suggest the correct command and provide a brief, one-sentence explanation.

    **User's Incorrect Command:**
    "{user_query}"

    **Relevant Documentation Snippets:**
    {context}

    **Your Suggestion:**
    (Provide the corrected command inside a markdown code block, followed by the explanation)
    """

    print("🧠 Asking Llama 3 for a suggestion...")
    
    try:
        response = ollama.chat(
            model=LLM_MODEL,
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        suggestion = response['message']['content']

        typer.secho("\n💡 Suggestion:", fg=typer.colors.GREEN, bold=True)
        print(suggestion)

    except Exception as e:
        typer.secho(f"Error: Could not connect to Ollama. Is it running? (ollama serve)", fg=typer.colors.RED)
        typer.secho(f"Details: {e}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()