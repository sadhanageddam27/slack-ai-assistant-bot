# Slack AI Assistant Bot

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Slack](https://img.shields.io/badge/Slack-Bolt%20SDK-4a154b?logo=slack)
![LLM](https://img.shields.io/badge/LLM-OpenAI%20Compatible-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

LLM-powered Slack bot that brings AI inference directly into Slack
workflows — natural language queries, real-time alerts, and text
summarization via slash commands. Built with Slack Bolt SDK and an
OpenAI-compatible backend that works with any local or cloud LLM.

## Live Project Page
**https://sadhanageddam27.github.io/slack-ai-assistant-bot/**

---

## Features

- `/ask <question>` — Query the LLM and get a formatted Block Kit response
- `/alert <message>` — Post structured alert notifications with sender context
- `/summarize <text>` — Summarize any text into 2–3 bullet points via LLM
- `@BotMention <question>` — Ask questions by mentioning the bot in any channel

---

## Project Structure

    slack-ai-assistant-bot/
    ├── app.py           # Slack Bolt app — slash commands and event handlers
    ├── llm.py           # LLM inference wrapper — swappable backend
    ├── requirements.txt # Python dependencies
    ├── .env.example     # Environment variable template
    └── README.md

---

## How It Works

    User types /ask in Slack
          │
          ▼
    Slack delivers event to app.py via Socket Mode
          │
          ▼
    app.py extracts query, calls ask_llm() in llm.py
          │
          ▼
    llm.py sends POST request to LLM API endpoint
          │
          ▼
    Response formatted using Slack Block Kit
          │
          ▼
    Structured message posted back to Slack channel

Socket Mode means no public server or webhook URL is needed —
the bot connects outbound to Slack and receives events in real time.

---

## Setup and Usage

**1. Clone and install**

    git clone https://github.com/sadhanageddam27/slack-ai-assistant-bot.git
    cd slack-ai-assistant-bot
    pip install -r requirements.txt

**2. Create a Slack App**

- Go to api.slack.com/apps and click Create New App
- Under OAuth and Permissions, add bot scopes: `chat:write`, `commands`, `app_mentions:read`
- Under Slash Commands, create `/ask`, `/alert`, and `/summarize`
- Under Socket Mode, enable it and generate an App-Level Token
- Install the app to your workspace and copy the Bot Token

**3. Configure environment variables**

    cp .env.example .env

Fill in your `.env` file:

    SLACK_BOT_TOKEN=xoxb-your-bot-token
    SLACK_APP_TOKEN=xapp-your-app-token
    OPENAI_API_KEY=your-openai-api-key

**4. Run**

    python app.py

---

## Using a Local LLM (Ollama)

Run fully offline — no OpenAI API key needed:

    LLM_BASE_URL=http://localhost:11434/v1
    LLM_MODEL=llama3
    OPENAI_API_KEY=ollama

Install Ollama from https://ollama.com, then pull a model with `ollama pull llama3`.

---

## Tech Stack
Python · Slack Bolt SDK · Slack Block Kit · REST API · Socket Mode · OpenAI API

## Topics
`python` `slack-api` `slack-bot` `llm` `openai` `rest-api`
`natural-language-processing` `automation` `bolt-sdk`
