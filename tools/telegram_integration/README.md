# Telegram Integration Tool

This tool enables your local LLMs in Open-WebUI to autonomously send formatted messages directly to your Telegram account. It is specifically optimized to handle Telegram's strict MarkdownV2 formatting, ensuring bold text, lists, and special characters don't crash the API.

## 📋 Prerequisites

Before installing this tool, you need a Telegram Bot Token and your destination Chat ID.

### 1. Get a Bot Token
1. Open Telegram and search for **@BotFather**.
2. Send the `/newbot` command and follow the prompts to give your bot a name and username.
3. Copy the **Bot Token** provided (it will look something like `123456789:ABCdefGHIjklMNOpqrSTUvwxYZ`).

### 2. Get Your Chat ID
1. **Crucial Step:** Search for your newly created bot in Telegram, start a chat, and send it a random message (like "Hello"). *If you skip this, the API won't have a chat history to pull your ID from.*
2. Open your web browser and go to this URL (replace `<YOUR_BOT_TOKEN>` with the token from step 1): 
   `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Look at the JSON response and find the `chat` block:
   ```json
   "chat": {
     "id": 123456789,
     "first_name": "Your Name",
     "type": "private"
   }
   ```
4. Copy that **id** number. (Make sure to include the minus sign `-` if you added the bot to a group chat).

---

## 🛠️ Installation

1. Open your Open-WebUI interface.
2. Navigate to **Workspace** (on the left sidebar) > **Tools**.
3. Click the **`+`** (Create Tool) button.
4. Name the tool (e.g., `Telegram Integration`).
5. Copy the entire contents of `telegram.py` from this repository and paste it into the code editor.
6. Click **Save**.

---

## ⚙️ Configuration (Valves)

Open-WebUI uses "Valves" to securely store your credentials so they aren't exposed in the code or to the model itself.

1. On the Tools page, find your newly created Telegram tool.
2. Click the **Gear Icon** (⚙️) to open the tool's settings.
3. Enter your **Bot Token** into the `TELEGRAM_BOT_TOKEN` field.
4. Enter your **Chat ID** into the `TELEGRAM_CHAT_ID` field.
5. Click **Save**.

---

## 🚀 Usage Examples

Start a new chat with a tool-capable model (like MLX variants of Qwen, Llama, or Mistral when you are on a Mac). Enable the tool by clicking the **`+`** icon next to the prompt input bar and toggling your Telegram tool on.

You can now ask the model to interact with your phone naturally:

* *"Summarize this long document and send the key bullet points to my Telegram."*
* *"Write a Python script for a simple web scraper, and send the final code to me on Telegram so I have it on my phone."*
* *"I am stepping away from the computer. When you finish generating this long research report, send me a notification on Telegram."*
