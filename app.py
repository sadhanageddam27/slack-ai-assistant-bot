import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from llm import ask_llm

# Initialize the Slack app with bot token
app = App(token=os.environ["SLACK_BOT_TOKEN"])


# ── /ask command ──────────────────────────────────────────────────────────────
# Usage: /ask What is the status of our deployment pipeline?
@app.command("/ask")
def handle_ask(ack, respond, command):
    ack()  # Acknowledge the command immediately

    user_query = command.get("text", "").strip()

    if not user_query:
        respond("Please provide a question. Example: `/ask What is the capital of France?`")
        return

    respond(f":hourglass_flowing_sand: Thinking about: *{user_query}*...")

    answer = ask_llm(user_query)

    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":mag: *Query:* {user_query}"
                }
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":robot_face: *Answer:*\n{answer}"
                }
            }
        ]
    )


# ── /alert command ────────────────────────────────────────────────────────────
# Usage: /alert Deployment pipeline is down in production
@app.command("/alert")
def handle_alert(ack, respond, command, client):
    ack()

    alert_message = command.get("text", "").strip()
    channel_id = command["channel_id"]
    user_id = command["user_id"]

    if not alert_message:
        respond("Please provide an alert message. Example: `/alert Server is down in production`")
        return

    # Post alert to the channel where command was triggered
    client.chat_postMessage(
        channel=channel_id,
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🚨 Alert Notification"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Message:* {alert_message}"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"Posted by <@{user_id}>"
                    }
                ]
            }
        ]
    )

    respond(":white_check_mark: Alert posted to the channel successfully.")


# ── /summarize command ────────────────────────────────────────────────────────
# Usage: /summarize Our Q3 revenue grew by 20%. Costs reduced by 10%. Team expanded.
@app.command("/summarize")
def handle_summarize(ack, respond, command):
    ack()

    text = command.get("text", "").strip()

    if not text:
        respond("Please provide text to summarize. Example: `/summarize <your text here>`")
        return

    respond(":hourglass_flowing_sand: Summarizing...")

    prompt = f"Summarize the following in 2-3 concise bullet points:\n\n{text}"
    summary = ask_llm(prompt)

    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":memo: *Summary:*\n{summary}"
                }
            }
        ]
    )


# ── App mention handler ───────────────────────────────────────────────────────
# Handles @BotName <question> in channels
@app.event("app_mention")
def handle_mention(event, say):
    user = event.get("user")
    text = event.get("text", "")

    # Strip the bot mention tag from the message
    query = text.split(">", 1)[-1].strip()

    if not query:
        say(f"Hey <@{user}>! Ask me anything using `/ask`, or mention me with a question.")
        return

    answer = ask_llm(query)

    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Hey <@{user}>! Here's what I found:\n\n{answer}"
                }
            }
        ]
    )


# ── Start the app ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    print("Slack AI Assistant Bot is running...")
    handler.start()
