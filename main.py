from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    print("Hello world!")
    print(f"{os.environ['LANGCHAIN_PROJECT']}")
