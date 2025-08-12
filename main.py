from openai import OpenAI
import os

from dotenv import load_dotenv
import json

load_dotenv()

MODEL = "gpt-oss:20b"


def get_client() -> OpenAI:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )
    return client


def load_tools(name: str) -> list[dict]:
    with open(f"tools/{name}.json", "r") as f:
        return json.load(f)


def get_weather(city: str) -> str:
    client = get_client()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": f"What is the weather in {city}?"},
        ],
    )
    data = response.choices[0].message.content
    
    print(data)
    return data


def main():
    client = get_client()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Hello, can you explain how I can integrate and use helm with kustomize",
            },
            {"role": "system", "content": "You are a senior devops engineer"},
        ],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
