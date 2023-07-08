import json


class Composer:
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

    def _get_user_content(self, content: str, title: str) -> str:
        json_body = json.dumps({"title": title, "content": content})
        return (
            f"Here is the message you need to deal with:\n\n```json\n{json_body}\n```"
        )

    def get_history_messages(self) -> list[dict]:
        return self.messages

    def get_markdown(self) -> str:
        markdown = ""
        for message in self.messages:
            markdown += f"**{message['role']}**:\n\n{message['content']}\n\n"
        return markdown

    def get_new_messages(self, content: str, title: str) -> list[dict]:
        return self.messages + [
            {"role": "user", "content": self._get_user_content(content, title)}
        ]
