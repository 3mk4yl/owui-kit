"""
title: Telegram Integration Tool
author: 3mk4yl (github.com/3mk4yl/owui-kit)
description: Allows an LLM to send and read messages via a Telegram bot.
version: 1.0
"""

import urllib.request
import urllib.parse
import json
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        TELEGRAM_BOT_TOKEN: str = Field(
            default="", description="Your Telegram Bot Token from @BotFather"
        )
        TELEGRAM_CHAT_ID: str = Field(
            default="", description="The default Chat ID to send messages to"
        )

    def __init__(self):
        # Initialize the Valves for secure credential storage
        self.valves = self.Valves()

    def send_telegram_message(self, message: str) -> str:
        """
        Sends a text message to the user via Telegram.
        Invoke this when you need to notify the user, send an alert, or deliver a requested message.

        :param message: The text message to send to Telegram.
        """
        token = self.valves.TELEGRAM_BOT_TOKEN
        chat_id = self.valves.TELEGRAM_CHAT_ID

        if not token or not chat_id:
            return "Error: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not configured in the tool valves."

        # 1. Convert standard LLM bold/italic to Telegram MarkdownV2 format
        # LLMs use **bold**, Telegram uses *bold*
        message = message.replace("**", "*")

        # 2. Escape special characters required by Telegram's MarkdownV2
        # (Excluding * and ` which are used for formatting)
        escape_chars = [
            "_",
            "[",
            "]",
            "(",
            ")",
            "~",
            ">",
            "#",
            "+",
            "-",
            "=",
            "|",
            "{",
            "}",
            ".",
            "!",
        ]
        for char in escape_chars:
            message = message.replace(char, f"\\{char}")

        url = f"https://api.telegram.org/bot{token}/sendMessage"

        # 3. Add parse_mode to the payload
        data = urllib.parse.urlencode(
            {"chat_id": chat_id, "text": message, "parse_mode": "MarkdownV2"}
        ).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode())
                if result.get("ok"):
                    return f"Successfully sent message to Telegram."
                else:
                    return f"Telegram API Error: {result.get('description')}"
        except Exception as e:
            return f"Failed to send Telegram message: {str(e)}"

    def read_telegram_messages(self, limit: int = 5) -> str:
        """
        Retrieves the latest messages sent by the user to the Telegram bot.
        Invoke this when the user asks you to check if they have any new Telegram messages.

        :param limit: The maximum number of recent messages to retrieve.
        """
        token = self.valves.TELEGRAM_BOT_TOKEN
        if not token:
            return "Error: TELEGRAM_BOT_TOKEN is missing in valves."

        url = f"https://api.telegram.org/bot{token}/getUpdates?limit={limit}"

        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode())
                if result.get("ok"):
                    messages = []
                    for update in result["result"]:
                        if "message" in update and "text" in update["message"]:
                            sender = update["message"]["from"].get("first_name", "User")
                            text = update["message"]["text"]
                            messages.append(f"{sender}: {text}")
                    return (
                        "\n".join(messages)
                        if messages
                        else "No new messages in Telegram."
                    )
                return "Error fetching messages from Telegram."
        except Exception as e:
            return f"Failed to get Telegram updates: {str(e)}"

