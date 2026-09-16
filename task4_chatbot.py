

import random

BOT_NAME = "AlphaBot"

# Exit words end the conversation
EXIT_WORDS = ["bye", "goodbye", "exit", "quit", "see you"]


def clean(text):
    """Normalise user input: lowercase, trimmed, no trailing punctuation."""
    return text.lower().strip().strip("!.?,")


def get_response(user_input):
    """Return the bot's reply for a given user message."""
    msg = clean(user_input)

    if msg in ["hello", "hi", "hey", "hii", "hello there"]:
        return random.choice(["Hi!", "Hello there!", "Hey, good to see you!"])

    elif msg in ["how are you", "how r u", "how are you doing"]:
        return "I'm fine, thanks! How about you?"

    elif msg in ["i am fine", "i'm fine", "good", "i am good", "fine"]:
        return "Glad to hear that!"

    elif msg in ["what is your name", "who are you", "your name"]:
        return f"My name is {BOT_NAME}. I'm a simple rule-based chatbot."

    elif msg in ["what can you do", "help"]:
        return ("I can reply to greetings, tell you my name, crack a joke, "
                "or say goodbye. Try: hello / how are you / your name / "
                "joke / bye")

    elif msg in ["joke", "tell me a joke", "make me laugh"]:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I would tell you a UDP joke, but you might not get it.",
            "There are 10 types of people: those who know binary and those who don't.",
        ])

    elif msg in ["thanks", "thank you", "thx"]:
        return "You're welcome!"

    elif msg in EXIT_WORDS:
        return "Goodbye! Have a great day."

    elif msg == "":
        return "You didn't type anything. Say something!"

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I know."


def chat():
    """Main conversation loop."""
    print("=" * 45)
    print(f"   {BOT_NAME} - CodeAlpha Task 4")
    print("   Type 'bye' to end the chat.")
    print("=" * 45)

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print(f"{BOT_NAME}: {reply}")

        if clean(user_input) in EXIT_WORDS:
            break


if __name__ == "__main__":
    chat()
