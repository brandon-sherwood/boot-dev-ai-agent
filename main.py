import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompt import system_prompt
from functions.call_function import available_functions
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User Prompt")
parser.add_argument("--verbose", action="store_true",
                    help="Enable verbose output")

args = parser.parse_args()
user_input = args.user_prompt

messages = [types.Content(
    role="user", parts=[types.Part(text=args.user_prompt)])]


def main():
    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )

        if response.candidates != None:
            for candidate in response.candidates:
                messages.append(candidate.content)
        else:
            print(response.text)

        break

        if api_key == None:
            raise RuntimeError("Environment variable not found!")

        if response.usage_metadata == None:
            raise RuntimeError("Failed API request")

        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        user_prompt = user_input

        if args.verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

        function_results = []
        if response.function_calls:
            for call in response.function_calls:
                function_call_result = call_function(
                    call, verbose=args.verbose)

                if not function_call_result.parts:
                    raise Exception("Parts list is empty!")

                if function_call_result.parts[0].function_response == None or function_call_result.parts[0].function_response.response == None:
                    raise Exception(
                        "The function_response or response in the list are None!")
                else:
                    function_results.append(function_call_result.parts[0])

                if args.verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}")

    else:
        print(response.text)


if __name__ == "__main__":
    main()
