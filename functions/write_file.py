import os


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
