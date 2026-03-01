import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', contents='"Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."'
)


def main():
    print("Hello from boot-dev-ai-agent!")

    if api_key == None:
        raise RuntimeError("Environment variable not found!")

    if response.usage_metadata == None:
        raise RuntimeError("Failed API request")

    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count

    print(f"Prompt tokens: {X}")
    print(f"Response tokens: {Y}")
    print(response.text)


if __name__ == "__main__":
    main()
