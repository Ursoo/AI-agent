import os
from config import MAX_READ_CHARS

def get_file_content(working_dir, file_path):
    absolute_file_path = os.path.abspath(os.path.join(working_dir, file_path))
    absolute_working_dir = os.path.abspath(working_dir)
    if not absolute_file_path.startswith(absolute_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(absolute_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(absolute_file_path, "r") as f:
            contents = f.read(MAX_READ_CHARS+1)
            if len(contents) > MAX_READ_CHARS:
                return contents[:MAX_READ_CHARS-1] + f'\n[...File "{file_path}" truncated at 10000 characters]'
            else:
                return contents
    except Exception as e:
        return f"Error: {e}"