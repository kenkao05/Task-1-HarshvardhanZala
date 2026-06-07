# Project 1 — Rule-Based AI Chatbot 🤖

**DecodeLabs AI Internship | Batch 2026**
**Intern:** Harshvardhan Zala
**Track:** Artificial Intelligence

---

## Overview

A rule-based chatbot built on **deterministic logic** — no machine learning, no neural networks, no hallucinations. Every response is traceable from input to output.

This project demonstrates the foundational architecture that acts as the **control layer** (guardrails) in modern AI systems — the same layer used by frameworks like NVIDIA NeMo and Llama Guard in production.

---

## Architecture — The IPO Model

```
INPUT          →      PROCESS         →      OUTPUT
(Raw Feed)            (Logic Skeleton)        (Feedback Loop)

Sanitization &    Intent Matching &      Response
Normalization         State               Generation
```

### Why a Dictionary, not if-elif?

| Approach | Complexity | Maintainability |
|---|---|---|
| if-elif ladder | O(n) — linear scan | High technical debt |
| Dictionary lookup | **O(1) — constant time** | Add a line, add an intent |

The if-elif ladder is explicitly an **anti-pattern** for this use case. A dictionary with `.get()` handles lookup + fallback in a single atomic operation.

---

## Project Specifications (Logic Skeleton)

- ✅ **INPUT LOOP** — Continuous `while True` cycle
- ✅ **SANITIZATION** — Handles case & whitespace (`lower().strip()`)
- ✅ **KNOWLEDGE BASE** — Dictionary with 20+ intents
- ✅ **FALLBACK** — Default response for unknown inputs
- ✅ **EXIT STRATEGY** — Clean break on `quit` / `exit` / `bye`

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python chatbot.py
```

**Example session:**
```
──────────────────────────────────────────────────
  DecodeLabs | Project 1 — Rule-Based AI Chatbot
  Type 'help' for topics  |  Type 'quit' to exit
──────────────────────────────────────────────────
BotX : Hello! I'm BotX. How can I help you today?

You  : what is ai
BotX : AI is the simulation of human intelligence by machines — enabling them to learn, reason, and solve problems.

You  : what is machine learning
BotX : Machine Learning is a subset of AI where systems learn patterns from data without being explicitly programmed.

You  : quit
BotX : Goodbye! Keep building. 🚀
──────────────────────────────────────────────────
```

---

## Concepts Demonstrated

- **Control Flow** — while loops, conditional branching
- **Data Structures** — Dictionary / Hash Map (O(1) lookup)
- **Input Sanitization** — Normalization before processing
- **Graceful Exit Handling** — KeyboardInterrupt + exit commands
- **IPO Model** — Input → Process → Output architecture
- **White Box AI** — Every decision is traceable and explainable

---

## Project Structure

```
decodelabs_ai_project1/
├── chatbot.py       # Main chatbot — fully documented
└── README.md        # This file
```

---

*DecodeLabs | Batch 2026 | Artificial Intelligence Track*
