"""
    Composer is responsible for handling messages. It can load messages from a configuration file,
    generate a user message, return the history of messages, generate a markdown string from the messages, and
    add a new message to the existing messages.
"""

import json


class Composer:
    
    # This function initializes the Composer class. It takes a configuration file as input.
    # The configuration file is opened and its content is loaded into the 'config' attribute.
    # An empty list is created for the 'messages' attribute.
    # Then, for each message in the configuration, if the message does not have a 'content' key,
    # the content is read from the file specified by the 'content_file' key and added to the message.
    # Finally, each message (with its 'role' and 'content') is appended to the 'messages' list.
    def __init__(self, config):
        with open(config) as f:
            self.config = json.load(f)
        self.messages = []
        for message in self.config:
            if not message.get("content", None):
                with open(message["content_file"], "r", encoding="utf-8") as f:
                    message["content"] = f.read()
            self.messages.append(
                {"role": message["role"], "content": message["content"]}
            )

    # This function takes a content and title as input, converts them into a JSON object,
    # and returns a formatted string that includes the JSON object.
    # The returned string is intended to be a user message that needs to be dealt with.
    def _get_user_content(self, content: str, title: str) -> str:
        json_body = json.dumps({"title": title, "content": content})
        return (
            f"Here is the message you need to deal with:\n\n```json\n{json_body}\n```"
        )

    # This function returns the history of messages
    def get_history_messages(self) -> list[dict]:
        return self.messages

    # This function generates a markdown string from the messages
    # Each message is formatted with the role in bold, followed by the content
    # The messages are separated by two newlines
    def get_markdown(self) -> str:
        markdown = ""
        for message in self.messages:
            markdown += f"**{message['role']}**:\n\n{message['content']}\n\n"
        return markdown

    # This function adds a new message to the existing messages
    # The new message is created with the role 'user' and the content is generated by the _get_user_content function
    def get_new_messages(self, content: str, title: str) -> list[dict]:
        return self.messages + [
            {"role": "user", "content": self._get_user_content(content, title)}
        ]
