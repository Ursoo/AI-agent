import os
from google.genai import types


def write_file(working_directory, file_path, content):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(
        os.path.join(working_directory, file_path))
    open_file_mode = "w"

    if not absolute_file_path.startswith(absolute_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_file_path):
        open_file_mode = "x"

    try:
        with open(absolute_file_path, open_file_mode) as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, creating it if it doesn't exist, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file that is supposed to be written to, relative to the working directory. If the file doesn't exist, it will be created. You MUST provide this.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text to be written to the file found or created at file_path."
            )
        },
    ),
)
