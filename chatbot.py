# ============================================================
#  DecodeLabs | AI Internship Batch 2026
#  Project 1  : Rule-Based AI Chatbot
#  Author     : Harshvardhan Zala
#  Track      : Artificial Intelligence
# ============================================================
#
#  Architecture: IPO Model (Input → Process → Output)
#  Pattern    : Dictionary-based O(1) lookup  [NOT if-elif ladder]
#  Ref Slide  : "The Anti-Pattern: The IF-ELIF Ladder" — DecodeLabs
# ============================================================


# ── PHASE 1 : KNOWLEDGE BASE ─────────────────────────────────
# The "White Box" — every rule is explicit and traceable.
# To add a new intent, just add a key-value pair here.

KNOWLEDGE_BASE = {
    # Greetings
    "hello"         : "Hey there! I'm BotX, your rule-based AI assistant. How can I help?",
    "hi"            : "Hi! What can I do for you today?",
    "hey"           : "Hey! Ask me anything.",
    "good morning"  : "Good morning! Hope you're having a great day.",
    "good evening"  : "Good evening! What's on your mind?",

    # Identity
    "who are you"   : "I'm BotX — a rule-based AI chatbot built on deterministic logic, not guesswork.",
    "what are you"  : "I'm a rule-based chatbot. No neural networks, no hallucinations — pure logic.",
    "your name"     : "My name is BotX.",

    # AI concepts (domain-relevant for the internship)
    "what is ai"            : "AI is the simulation of human intelligence by machines — enabling them to learn, reason, and solve problems.",
    "what is machine learning" : "Machine Learning is a subset of AI where systems learn patterns from data without being explicitly programmed.",
    "what is deep learning" : "Deep Learning uses multi-layered neural networks to model complex patterns in large datasets.",
    "what is a chatbot"     : "A chatbot is a program that simulates conversation with humans using either rules or AI models.",
    "rule based vs ai"      : "Rule-based systems are deterministic and traceable. AI/ML systems are probabilistic and adaptive. Both have a place.",

    # DecodeLabs context
    "what is decodelabs"    : "DecodeLabs is an industry training platform that bridges the gap between learning code and building real projects.",
    "what is this project"  : "This is Project 1 of your DecodeLabs AI internship — a Rule-Based Chatbot demonstrating control flow and logic.",

    # Small talk
    "how are you"           : "I'm running perfectly — 0 errors, 0 hallucinations. Thanks for asking!",
    "what can you do"       : "I can answer questions about AI, ML, chatbots, and have a basic conversation. Type 'help' for topics.",
    "help"                  : "Try asking: 'what is AI', 'what is machine learning', 'who are you', 'what is DecodeLabs', or just say 'hello'.",
    "thank you"             : "You're welcome! Is there anything else?",
    "thanks"                : "Anytime!",
}

EXIT_COMMANDS = {"quit", "exit", "bye", "goodbye", "stop"}

FALLBACK_RESPONSE = "I don't understand that yet. Type 'help' to see what I can answer."

SEPARATOR = "─" * 50


# ── PHASE 2 : IPO FUNCTIONS ───────────────────────────────────

def sanitize(raw: str) -> str:
    """
    INPUT phase — Sanitization & Normalization.
    Converts raw user input to a clean, comparable string.
    Ref slide: 'Phase 1: Input & Sanitization'
    """
    return raw.lower().strip()


def get_response(clean_input: str) -> str:
    """
    PROCESS phase — Intent Matching & State.
    Uses O(1) dictionary lookup instead of O(n) if-elif ladder.
    Ref slide: 'The Pivot: Hash Maps & Dictionaries'
    """
    return KNOWLEDGE_BASE.get(clean_input, FALLBACK_RESPONSE)


def display(message: str) -> None:
    """
    OUTPUT phase — Response Generation & Feedback Loop.
    """
    print(f"BotX : {message}")


# ── PHASE 3 : THE HEARTBEAT (INFINITE LOOP) ───────────────────

def run():
    """
    The continuous while-loop that keeps the chatbot alive
    until an explicit exit/kill command is received.
    Ref slide: 'The Heartbeat: The Infinite Loop'
    """
    print(SEPARATOR)
    print("  DecodeLabs | Project 1 — Rule-Based AI Chatbot")
    print("  Type 'help' for topics  |  Type 'quit' to exit")
    print(SEPARATOR)

    display("Hello! I'm BotX. How can I help you today?")
    print()

    while True:
        try:
            raw_input_text = input("You  : ")
        except (EOFError, KeyboardInterrupt):
            # Graceful exit on Ctrl+C or piped input ending
            print()
            display("Session ended. Goodbye!")
            break

        clean_input = sanitize(raw_input_text)

        # EXIT STRATEGY — clean break command
        # Ref slide: 'Project 1 Specification: The Logic Skeleton'
        if clean_input in EXIT_COMMANDS:
            display("Goodbye! Keep building. 🚀")
            print(SEPARATOR)
            break

        if not clean_input:
            continue  # ignore empty input, don't waste a response

        reply = get_response(clean_input)
        display(reply)
        print()


# ── ENTRY POINT ───────────────────────────────────────────────

if __name__ == "__main__":
    run()
