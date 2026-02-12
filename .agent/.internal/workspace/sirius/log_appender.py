import datetime
import os
import sys

# Usage: python3 log_appender.py <log_path> <content_file>
# content_file should contain the full log entry including the footer placeholder if any.
# However, to be safe and standard, this script will append the timestamp footer automatically.

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 log_appender.py <log_path> <content_file>")
        sys.exit(1)

    log_path = sys.argv[1]
    content_file = sys.argv[2]

    # Read content
    try:
        with open(content_file, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Content file '{content_file}' not found.")
        sys.exit(1)

    # Generate timestamp
    # Format: 2026-02-12T22:50:00+09:00
    timestamp = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    
    # Add footer
    # Footer format: > [TIMESTAMP: Identifier]
    # We assume identifier is "Lico (Sirius)" for this session, but maybe we should pass it?
    # For now, hardcoding based on current persona or passing as arg is better.
    # Let's pass it as arg 3.
    
    identifier = "Lico (Sirius)"
    if len(sys.argv) > 3:
        identifier = sys.argv[3]

    footer = f"\n> [{timestamp}: {identifier}]\n"
    
    final_content = content + footer

    # Append to log
    try:
        with open(log_path, "a") as f:
            f.write(final_content)
        print(f"Successfully appended to {log_path}")
    except FileNotFoundError:
        # Try to ensure directory exists? No, protocol says structure should exist.
        print(f"Error: Log file '{log_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
