"""
This file contains the Generator class which is used to generate responses using the OpenAI API.
The Generator class takes a configuration and a maximum retry count as input.
It uses the Composer class to get new messages and then tries to generate a response using the OpenAI API.
If the generation fails, it retries up to the maximum retry count.
If it still fails after the maximum retries, it raises an exception.
The generated response is then parsed and returned as a dictionary.
"""

import openai
from examples.composer import Composer
import json
import os
# import re

if os.environ.get("OPENAI_API_BASE", None):
    openai.api_base = os.environ["OPENAI_API_BASE"]


class Generator:
    def __init__(self, config: str, max_retry: int = 3):
        self.composer = Composer(config=config)
        self.max_retry = max_retry

    def generate(self, response_dict: str, title: str, model="gpt-3.5-turbo-16k") -> dict:
        messages = self.composer.get_new_messages(content=response_dict, title=title)
        retry_count = 0
        while retry_count < self.max_retry:
            try:
                response = openai.ChatCompletion.create(
                    model=model, messages=messages
                )
                response_dict = response["choices"][0]["message"]["content"]
                # pattern = r"\{(.*?)\}"
                # match = re.search(pattern, response_dict, flags=re.DOTALL)
                response_dict = json.loads(response_dict)
                assert "title" in response_dict
                assert "content" in response_dict
                assert "reason" in response_dict
                break
            except Exception as e:
                print(e)
                retry_count += 1
                continue
        if retry_count >= self.max_retry:
            raise Exception(f"Failed to generate content after max_retry={self.max_retry}")
        return response_dict
