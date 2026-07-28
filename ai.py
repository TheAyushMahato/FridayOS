import requests
from brain_ai import build_prompt

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen3:4b"

# Stores conversation history
conversation_history = ""


def ask_ai(user_message):
    global conversation_history

    # Add user message
    conversation_history += f"\nAyush: {user_message}\n"

    # Build final prompt
    prompt = build_prompt(conversation_history)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=90
        )

        response.raise_for_status()

        reply = response.json().get("response", "").strip()

        # Remove thinking tags if model outputs them
        if "...done thinking." in reply:
            reply = reply.split("...done thinking.")[-1].strip()

        # Save assistant reply
        conversation_history += f"Friday: {reply}\n"

        # Prevent unlimited memory growth
        if len(conversation_history) > 12000:
            conversation_history = conversation_history[-8000:]

        return reply

    except requests.exceptions.ConnectionError:
        return "I can't reach Ollama. Please make sure it is running."

    except requests.exceptions.Timeout:
        return "The AI is taking too long to respond."

    except Exception as e:
        return f"AI Error: {e}"


def clear_history():
    global conversation_history
    conversation_history = ""