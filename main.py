from openai import OpenAI
import os

from dotenv import load_dotenv
import json
from loguru import logger

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
    logger.info(f"Getting weather for {city}")

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": f"What is the weather in {city}?"},
            ],
        )
        data = response.choices[0].message.content
        logger.info(f"Weather response: {data}")
        print(data)
        return data
    except Exception as e:
        logger.error(f"Error getting weather: {e}")
        return f"Sorry, I couldn't get the weather for {city}. Error: {e}"


def main():
    client = get_client()
    logger.info("Starting main conversation")

    try:
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
    except Exception as e:
        logger.error(f"Error in main conversation: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
