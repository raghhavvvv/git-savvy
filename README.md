# Git Savvy 🧠

A local-first, AI-powered command-line tool that suggests fixes for incorrect Git commands. Instead of just getting `git: 'comit' is not a git command`, get an instant, intelligent suggestion.

![Demo of Git Savvy in action](https://github.com/raghhavvvv/git-savvy/blob/main/assets/works.mov.gif?raw=true)
## How It Works

`git-savvy` uses a **RAG (Retrieval-Augmented Generation)** pipeline running entirely on your local machine:

1.  **Retrieval:** When you provide an incorrect command, it's converted into a vector and used to search a local **ChromaDB** database for relevant documentation and common error patterns.
2.  **Generation:** The user's query and the retrieved context are then fed into a locally running **Llama 3 8B** model (via Ollama) to generate a helpful correction and explanation.
3.  **Local First:** No data ever leaves your machine. Your command history and queries remain private.

## Tech Stack

-   **Language:** Python
-   **CLI Framework:** Typer
-   **LLM:** Llama 3 8B
-   **LLM Runner:** Ollama
-   **Vector Database:** ChromaDB
-   **Embedding Model:** Sentence-Transformers

## Getting Started

### Prerequisites

-   Python 3.8+
-   [Ollama](https://ollama.com/) installed and running.
-   The Llama 3 8B model pulled: `ollama pull llama3:8b`

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/git-savvy.git
    cd git-savvy
    ```

2.  **Set up a virtual environment and install dependencies:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt 
    ```
    *(Note: You will need to create a `requirements.txt` file first. See "Creating a requirements.txt" below.)*

3.  **Build the knowledge base:**
    This script populates the local vector database. You only need to run this once.
    ```bash
    python3 ingest.py
    ```

### Usage

To get a suggestion for a faulty command:

```bash
python3 savvy.py "git comit -m 'my feature'"
