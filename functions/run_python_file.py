import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(
        os.path.join(working_directory, file_path))

    if not absolute_file_path.startswith(absolute_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    arguments = ["uv", "run", f"{absolute_file_path}"]
    if args:
        arguments.append(*args)

    try:
        result = subprocess.run(
            args=arguments, timeout=30, capture_output=True)
        result_strings_list = []
        if result.stdout:
            result_strings_list.append(f"STDOUT: {result.stdout}")
        else:
            result_strings_list.append("No output produced.")
        result_strings_list.append(f"STDERR: {result.stderr}")
        if result.returncode != 0:
            result_strings_list.append(
                f"Process exited with code {result.returncode}")
        return "\n".join(result_strings_list)
    except Exception as e:
        return f"Error: executing Python file: {e}"
