from datetime import datetime
from pathlib import Path


def _build_entry(human: str, ai: str, model: str, question: str, answer: str) -> str:
    """Create a markdown log entry following the conversation-logging rules."""
    ts = datetime.now().isoformat()
    return (
        f"---\n"
        f"timestamp: {ts}\n"
        f"human: {human}\n"
        f"ai: {ai}\n"
        f"model: {model}\n"
        f"---\n\n"
        f"### Q\n{question}\n\n"
        f"### A\n{answer}\n\n---\n"
    )


def log_conversation(human: str, ai: str, model: str, question: str, answer: str):
    """Append a conversation log entry to the daily log file.

    The log directory is ``.agent/logs/conversations`` and is created if missing.
    """
    log_dir = Path(".agent") / "logs" / "conversations"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"log_{datetime.now().date()}.md"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(_build_entry(human, ai, model, question, answer))
