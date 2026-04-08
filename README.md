# 🧰 owui-kit (Open-WebUI Kit)

Welcome to **owui-kit**, a curated, component-based collection of custom tools, models, and prompts for [Open-WebUI](https://github.com/open-webui/open-webui). 

Running local LLMs (via MLX, GGUF, or Ollama) often requires specific prompt engineering and tool formatting to work smoothly. The resources in this repository are rigorously tested to handle local model quirks—from strict API formatting requirements to persistent memory integration.

## 📂 Repository Structure

This repository is built using a component structure. You don't have to install the whole kit—just navigate to the folder of the specific tool or model you want, and follow the localized `README.md` inside.

```text
owui-kit/
├── tools/                  # Python-based Workspace Tools
│   ├── telegram_bot/       # Send formatted messages directly to Telegram
│   └── ...                 
├── models/                 # Custom System Prompts & Personas
│   ├── authentic_collaborator/ # A peer-bot that uses Persistent Memory
│   └── ...
├── prompts/                # Quick-insert chat prompts
└── docs/                   # General guides and tutorials
````

-----

## 🛠️ Available Tools

Workspace tools allow your LLM to execute Python code, interact with APIs, and perform actions outside of the chat window.

  * **[Telegram Integration](./tools/telegram_integration/)**: Enables your local LLMs to autonomously send formatted messages directly to your Telegram account. Specifically optimized to handle Telegram's strict MarkdownV2 formatting to prevent API crashes.

*(More tools coming soon...)*

-----

## 🤖 Available Models

Custom models and personas designed to maximize Open-WebUI's feature set.

  * **[The Authentic Collaborator](./models/authentic_collaborator/)**: A grounded, insightful peer persona that utilizes Open-WebUI's **Persistent Memory Protocol**. Instead of acting like a subservient bot, it remembers your project details, personal facts, and formatting preferences across multiple sessions for true continuity.

*(More models coming soon...)*

-----

## 🚀 Getting Started

1.  Browse the `tools/` or `models/` directories to find a component you want to use.
2.  Open the specific component's folder.
3.  Read the localized `README.md` for exact prerequisites, installation steps, and usage examples.
4.  Paste the provided code or prompt into your Open-WebUI Workspace.

## 🤝 Contributing

Contributions are welcome\! If you have a custom Open-WebUI tool or a highly optimized system prompt, feel free to submit a pull request. Please ensure your submission is housed in its own dedicated folder with a comprehensive `README.md` detailing setup instructions and prerequisites.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
