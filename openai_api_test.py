import os

from dotenv import load_dotenv
from openai import OpenAI


def api_test(client: OpenAI) -> None:
    """
    # Checking whether API is working
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hi"}]
        )
        print("API key is working! Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Something went wrong: {e}")


def get_list_of_accessible_models(client: OpenAI) -> None:
    """
    Finding which model has access to the API
    """
    try:
        models = client.models.list()
        print("Accessible models:")
        for model in models.data:
            print(model.id)
    except Exception as e:
        print(f"Failed to fetch models: {e}")


def check_specific_model(client: OpenAI) -> None:
    # Checking specific model for access from the list above
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Or any model you're testing
            messages=[{"role": "user", "content": "Hello, can you hear me?"}]
        )
        print("You have access to this model!")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"No access to this model or error occurred: {e}")


if __name__ == '__main__':
    load_dotenv()

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # Initialize the OpenAI client with your API key
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

    api_test(openai_client)
    get_list_of_accessible_models(openai_client)
    check_specific_model(openai_client)
