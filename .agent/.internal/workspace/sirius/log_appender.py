import datetime
import os
import sys

# Usage: python3 log_appender.py <log_path> <content_file> <identifier>
# 
# Functionality:
# 1. Reads content from <content_file>.
# 2. Replaces '{{TIMESTAMP}}' with the current ISO8601 timestamp (with timezone).
# 3. Appends the processed content to <log_path>.
# 
# Changes (v2.0):
# - Removed automatic footer generation (as per agreement).
# - Added {{TIMESTAMP}} injection for dynamic header generation.

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 log_appender.py <log_path> <content_file> [identifier]")
        sys.exit(1)

    log_path = sys.argv[1]
    content_file = sys.argv[2]
    
    # Identifier is no longer used for footer, but kept in argv for compatibility/future use
    identifier = "Lico"
    if len(sys.argv) > 3:
        identifier = sys.argv[3]

    # Read content
    try:
        with open(content_file, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Content file '{content_file}' not found.")
        sys.exit(1)

    # Generate timestamp
    # Format: 2026-02-13T14:24:00+09:00
    timestamp = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    
    # Inject timestamp
    final_content = content.replace("{{TIMESTAMP}}", timestamp)
    
    # Ensure newline at the end if not present (optional, but good for logs)
    if not final_content.endswith("\n"):
        final_content += "\n"

    # Append to log
    try:
        with open(log_path, "a") as f:
            f.write(final_content)
        print(f"Successfully appended to {log_path}")
    except FileNotFoundError:
        print(f"Error: Log file '{log_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
