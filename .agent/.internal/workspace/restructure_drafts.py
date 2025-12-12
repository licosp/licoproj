import os
import re

TARGET_DIR = "/home/USER/develop/shared/project/licoproj/.human/users/leonidas/drafts"

def get_backtick_delimiter(content_lines):
    """
    Finds the longest sequence of backticks in the content and returns a delimiter 
    with one more backtick. Default is 3.
    """
    max_count = 0
    full_text = "".join(content_lines)
    matches = re.findall(r'`+', full_text)
    if matches:
        max_count = max(len(m) for m in matches)
    
    needed = max(3, max_count + 1)
    return "`" * needed

def process_file(filepath):
    print(f"Processing: {filepath}")
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    
    # Frontmatter handling
    idx = 0
    if lines and lines[0].strip() == "---":
        new_lines.append(lines[0])
        idx = 1
        while idx < len(lines):
            line = lines[idx]
            new_lines.append(line)
            idx += 1
            if line.strip() == "---":
                break
    
    # Reset query count per file
    query_count = 1
    
    body_lines = lines[idx:]
    buffer = []
    
    def flush_buffer():
        nonlocal query_count
        if not buffer:
            return
        
        # Determine title from first line
        first_line = buffer[0].strip()
        clean_title = first_line.replace("#", "").strip()
        title = (clean_title[:30] + '...') if len(clean_title) > 30 else clean_title
        if not title: title = "Untitled"
        
        delimiter = get_backtick_delimiter(buffer)
        
        new_lines.append(f"\n### Query {query_count}: {title}\n")
        new_lines.append(f"{delimiter}text\n")
        new_lines.extend(buffer)
        if buffer and not buffer[-1].endswith('\n'):
            new_lines.append('\n')
        new_lines.append(f"{delimiter}\n")
        
        query_count += 1
        buffer.clear()

    for line in body_lines:
        stripped = line.strip()
        
        # Check for Headers
        if stripped.startswith('#'):
            flush_buffer()
            new_lines.append("\n" + line.rstrip() + "\n") 
            continue
            
        # Check for Empty lines (separator)
        if not stripped:
            if buffer:
                flush_buffer()
            continue
        
        # Text line
        buffer.append(line)
    
    flush_buffer() # End of file
    
    output_path = filepath.replace(".md", "_structured.md")
    with open(output_path, 'w') as f:
        f.writelines(new_lines)

files = [f for f in sorted(os.listdir(TARGET_DIR)) if f.startswith('draft_') and f.endswith('.md') and '_structured' not in f]

for f in files:
    try:
        process_file(os.path.join(TARGET_DIR, f))
    except Exception as e:
        print(f"Failed to process {f}: {e}")
