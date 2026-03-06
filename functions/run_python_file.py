import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        target_dir = os.path.dirname(target_file)

        valid_target_path = os.path.commonpath(
            [abs_path, target_file]) == abs_path

        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args != None:
            command.extend(args)

        result = subprocess.run(command, cwd=abs_path,
                                capture_output=True, text=True, timeout=30)

        output_result = []
        if result.returncode != 0:
            output_result.append(
                f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output_result.append("No output produced")

        if result.stdout:
            output_result.append(f"STDOUT:\n{result.stdout}")

        if result.stderr:
            output_result.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output_result)

    except Exception as e:
        return f"Error: executing Python file: {e}"
