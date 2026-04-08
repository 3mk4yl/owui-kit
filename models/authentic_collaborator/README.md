# The Authentic Collaborator 

This repository/model configuration contains the system prompt for **The Authentic Collaborator**, a custom persona designed for Open-WebUI. Rather than acting as a subservient bot or a rigid lecturer, this model functions as a grounded, insightful, and adaptable peer. It balances empathy with candor, matching your conversational energy while synthesizing high-value insights.

**Key Feature: Persistent Memory**
This prompt is specifically designed to leverage Open-WebUI's memory capabilities. Through the **Persistent Memory Protocol**, the bot maintains context across multiple interactions. It will remember your project details, personal facts, and formatting preferences, treating them as "High Priority" context to ensure continuity and consistency in every future session.

---

## 📋 Prerequisites

To fully utilize the Persistent Memory Protocol defined in this prompt, you must be using a backend LLM that supports **Tool Use / Function Calling** (e.g., Llama 3.1, GPT-4o, Claude 3.5 Sonnet, etc.). The memory feature in Open-WebUI relies on the model's ability to seamlessly call internal memory tools to store and retrieve context.

---

## ⚙️ Activating the Memory System

Before engaging with the model, ensure that Open-WebUI's memory system is enabled for your account:

1. Click on your **User Name** in the bottom left corner of the Open-WebUI interface.
2. Select **Settings** from the menu.
3. Navigate to the **Personalization** tab.
4. Toggle the **Memory System** switch to **ON**.

---

## 🚀 Installation

To create this bot in your Open-WebUI instance, follow these steps:

1. Navigate to the **Workspace** tab in Open-WebUI.
2. Go to the **Models** section.
3. Click the **+** (Create a Model) button.
4. Give your model a name (e.g., `Authentic Collaborator`).
5. Select a capable base model (ensure it supports tool use, as noted in the prerequisites).
6. Copy the entire system prompt provided above and paste it into the **System Prompt** field.
7. Click **Save & Create**.

---

## 💬 Example Prompts

Here are a few ways to invoke the tool and test its persistent memory capabilities:

### 1. Storing a Preference
Establish a baseline for how you want the bot to work with you.
> *"For all future coding tasks, please remember that I exclusively use Python, and I strictly enforce type hinting and docstrings."*

### 2. Testing Memory Recall
Start a new chat session later and ask a question relying on the previously stored preference.
> *"Can you write a quick script that fetches the current weather from a public API?"* > *(The bot should automatically write it in Python with type hinting and docstrings).*

### 3. Storing Personal/Project Context
Give the bot specific details about your current workflow.
> *"Just so you know, I am currently working on a sci-fi novel called 'Neon Dawn'. The main character is a cynical detective named Elias."*

### 4. Retrieving Project Context
In a subsequent session, seamlessly continue your work without needing to re-explain the premise.
> *"Can you draft a brief dialogue scene where my main character interrogates a suspect in a rainy alleyway?"*
