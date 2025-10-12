import os


def get_files_info(working_dir, directory="."):
    absolute_working_directory = os.path.abspath(working_dir)
    absolute_file_path = os.path.abspath(os.path.join(working_dir, directory))

    if not absolute_file_path.startswith(absolute_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(absolute_file_path):
        return f'Error: "{directory}" is not a directory'

    try:
        results_list = []
        for element in os.listdir(absolute_file_path):
            elem_path = os.path.join(absolute_file_path, element)
            element_size = os.path.getsize(elem_path)
            is_dir = os.path.isdir(elem_path)
            results_list.append(
                f"- {element}: file_size= {element_size} bytes, is_dir={is_dir}")

        return '\n'.join(results_list)
    except Exception as e:
        return f"Error: {e}"
