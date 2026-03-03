import os


def get_files_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path, directory))

    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
