from anthropic import Anthropic
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()


class ClaudeComputerUse:
    def __init__(self):
        self.client = Anthropic(
            api_key=os.getenv('ANTHROPIC_API_KEY')
        )

    def test_computer_use(self):
        try:
            response = self.client.beta.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                tools=[
                    {
                        "type": "computer_20241022",
                        "name": "computer",
                        "display_width_px": 1024,
                        "display_height_px": 768,
                        "display_number": 1,
                    },
                    {
                        "type": "text_editor_20241022",
                        "name": "str_replace_editor"
                    },
                    {
                        "type": "bash_20241022",
                        "name": "bash"
                    }
                ],
                messages=[
                    {
                        "role": "user",
                        "content": "Create a Python file called hello.py that prints 'Hello, Computer Use!'"
                    }
                ],
                betas=["computer-use-2024-10-22"]
            )

            # Print the response
            print("Claude's Response:")
            print(response)

        except Exception as e:
            print(f"Error Type: {type(e).__name__}")
            print(f"Error Details: {str(e)}")
            if hasattr(e, 'response'):
                print("\nAPI Response Details:")
                print(json.dumps(e.response, indent=2))


def main():
    claude = ClaudeComputerUse()
    claude.test_computer_use()


if __name__ == "__main__":
    main()