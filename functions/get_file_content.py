import os
from config import MAX_READ_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(
        os.path.join(working_directory, file_path))

    if not absolute_file_path.startswith(absolute_working_directory):
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


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content present in a specific file found at a given path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where the file is found, relative to the working directory. You MUST provide this.",
            ),
        },
    ),
)
