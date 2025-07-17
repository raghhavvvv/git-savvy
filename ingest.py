import chromadb

GIT_DOCS = [
    {
        "id": "commit-typo",
        "document": "Common typo: 'comit' or 'commmit'. The correct command is 'git commit'. Use 'git commit -m \"Your message\"' to commit with a message."
    },
    {
        "id": "push-typo",
        "document": "Common typo: 'psuh'. The correct command is 'git push'. Use 'git push origin <branch-name>' to push a branch to a remote named 'origin'."
    },
    {
        "id": "status-command",
        "document": "To see the working tree status (which files are staged, unstaged, or untracked), use 'git status'."
    },
    {
        "id": "add-command",
        "document": "To add file contents to the index (staging area), use 'git add <file>'. To add all changed files, use 'git add .'."
    },
    {
        "id": "log-command",
        "document": "To view the commit history, use 'git log'. For a more compact view, use 'git log --oneline'."
    },
    {
        "id": "branch-command",
        "document": "To list all branches, use 'git branch'. To create a new branch, use 'git branch <branch-name>'. To switch to a branch, use 'git checkout <branch-name>' or 'git switch <branch-name>'."
    },
    {
        "id": "checkout-command",
        "document": "To switch branches or restore working tree files, use 'git checkout'. To switch to a new branch you are creating, use 'git checkout -b <new-branch-name>'."
    },
    {
        "id": "undo-commit",
        "document": "To undo the last commit but keep the changes in your working directory, use 'git reset --soft HEAD~1'. The changes will be staged and ready for a new commit."
    },
    {
        "id": "remote-command",
        "document": "To manage remote repositories, use 'git remote'. To see your current remotes, use 'git remote -v'. To add a new remote, use 'git remote add <name> <url>'."
    }
]

def main():

    print("🚀 Starting data ingestion...")

    client = chromadb.PersistentClient(path="db")


    collection = client.get_or_create_collection(name="git_knowledge")

    documents = [doc["document"] for doc in GIT_DOCS]
    ids = [doc["id"] for doc in GIT_DOCS]

    collection.add(
        documents=documents,
        ids=ids
    )

    print(f"✅ Ingestion complete. Added {len(ids)} documents to the 'git_knowledge' collection.")
    print("You can now run the main application.")

if __name__ == "__main__":
    main()