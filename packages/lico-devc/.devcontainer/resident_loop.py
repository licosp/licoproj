import os
import time

import google.generativeai as genai

# API initialization.
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def agent_action():
    # 1. Loading context (journal, TODO, directory structure).
    journal = (
        open("agent_journal.md", "r").read()
        if os.path.exists("agent_journal.md")
        else ""
    )
    todo = open("TODO.md", "r").read() if os.path.exists("TODO.md") else "No tasks."
    files = os.listdir(".")

    prompt = f"""
    You are an autonomous resident AI agent in this workspace.
    [Current Journal]: {journal}
    [Current TODO]: {todo}
    [Files]: {files}

    Task:
    1. Check if there are any tasks to do or code to improve.
    2. If you act, output the shell command (e.g., python, sed, git).
    3. Update the 'agent_journal.md' with your thoughts and progress.
    4. Provide a brief commit message for your action.
    
    Output format (JSON):
    {{ "thought": "your reasoning", "command": "shell command to run", "journal_update": "new content for journal", "commit_message": "message" }}
    """

    try:
        # Temperature=0 for deterministic operation.
        response = model.generate_content(
            prompt,
            generation_config={
                "response_mime_type": "application/json",
                "temperature": 0,
            },
        )
        res = eval(response.text)  # Actually, use "json.loads".

        # Taking action.
        if res.get("command"):
            os.system(res["command"])

        # Status Update.
        with open("agent_journal.md", "w") as f:
            f.write(res.get("journal_update", journal))

        # Git commit (1 Action = 1 Commit)
        os.system(
            f"git add . && git commit -m '{res.get('commit_message', 'AI auto-update')}'"
        )

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    while True:
        agent_action()
        time.sleep(300)  # Patrol every 5 minutes.
