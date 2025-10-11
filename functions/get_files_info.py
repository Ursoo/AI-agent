import os


def get_files_info(working_dir, directory="."):
    abs_path = os.path.abspath(working_dir)
    print("Absolute working directory path: " + abs_path)
    our_path = os.path.abspath(os.path.join(working_dir, directory))
    print("Absolute target directory path: " + our_path)
    try:
        if not our_path.startswith(abs_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(our_path):
            return f'Error: "{directory}" is not a directory'
        results_list = []
        for element in os.listdir(our_path):
            elem_path = os.path.join(our_path, element)
            element_size = os.path.getsize(elem_path)
            is_dir = os.path.isdir(elem_path)
            results_list.append(f"- {element}: file_size= {element_size} bytes, is_dir={is_dir}")
            
        return '\n'.join(results_list)
    except Exception as e:
        return f"Error: {e}"
