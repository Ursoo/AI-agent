import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_file
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
if len(sys.argv) == 1:
    print("please provide a prompt")
    exit(1)
prompt = sys.argv[1]
messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)


def run():
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages, config= types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT))
    return response


def main():

    response = run()
    if "--verbose" in sys.argv:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(
            f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
