# Slack AI Assistant Bot

A Python-based Slack bot that integrates LLM inference directly into Slack workflows. Supports natural language queries, real-time alerts, and text summarization via slash commands — built with Slack Bolt SDK and an OpenAI-compatible API backend.

---

## Features

- `/ask <question>` — Send any natural language query to the LLM and get a formatted response posted back to Slack
- `/alert <message>` — Post a structured alert notification to the current channel with sender context
- `/summarize <text>` — Summarize any block of text into concise bullet points using LLM inference
- `@BotMention <question>` — Mention the bot directly in any channel to ask a question

---

## Tech Stack

- **Python** — Core application logic
- **Slack Bolt SDK** — Slack event handling and slash command routing
- **Slack API (Block Kit)** — Rich message formatting
- **REST API** — LLM inference via OpenAI-compatible endpoint
- **Socket Mode** — Real-time event delivery without a public server

---

## Project Structure

```
slack-ai-assistant-bot/
├── app.py              # Slack Bolt app — slash commands and event handlers
├── llm.py              # LLM inference wrapper (swappable backend)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
└── README.md
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/sadhanageddam27/slack-ai-assistant-bot.git
cd slack-ai-assistant-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Slack App

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and click **Create New App**
2. Choose **From Scratch**, give it a name, select your workspace
3. Under **OAuth & Permissions**, add these Bot Token Scopes:
   - `chat:write`
   - `commands`
   - `app_mentions:read`
4. Under **Slash Commands**, create `/ask`, `/alert`, and `/summarize`
5. Under **Socket Mode**, enable it and generate an App-Level Token
6. Install the app to your workspace and copy the Bot Token

### 4. Configure environment variables

```bash
cp .env.example .env
# Fill in your SLACK_BOT_TOKEN, SLACK_APP_TOKEN, and OPENAI_API_KEY
```

### 5. Run the bot

```bash
python app.py
```

---

## Using a Local LLM (Ollama)

To run fully offline without an OpenAI key, install [Ollama](https://ollama.com) and set these in your `.env`:

```
LLM_BASE_URL=http://localhost:11434/v1
LLM_MODEL=llama3
OPENAI_API_KEY=ollama
```

---

## How It Works

```
User types /ask in Slack
        │
        ▼
Slack sends event to app.py via Socket Mode
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
```

---

## Example Output

**`/ask` command:**
> 🔍 **Query:** What are the benefits of microservices?
>
> 🤖 **Answer:**
> - Independent deployment and scaling per service
> - Technology flexibility across teams
> - Fault isolation — one service failure doesn't bring down the system

**`/alert` command:**
> 🚨 **Alert Notification**
> **Message:** Production deployment failed on service-api
> *Posted by @sadhana*

---

## License

MIT License
