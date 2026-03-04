import os


def write_file(working_directory, file_path, content):
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        target_dir = os.path.dirname(target_file)

        valid_target_path = os.path.commonpath(
            [abs_path, target_file]) == abs_path

        if valid_target_path == False:
            f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            f'Error: Cannot write to "{file_path}" as it is a directory'

    except:
        pass
