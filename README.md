# 🤖 AI Telegram Assistant & Personal Dashboard

An intelligent personal assistant bot built on Telegram that acts as your **Second Brain**. It automatically classifies user messages, parses financial transactions (expenses), summarizes reminders (notes) using **Gemini 2.5 Flash**, and saves them to a structured database.

This project is designed as an end-to-end full-stack portfolio application, showcasing modern AI integration, structured data validation, and async backend engineering.

---

## 🌟 Key Features

* **Multi-Modal AI Classifier:** Intelligently categorizes incoming text into `expense`, `note`, or `other` using **Google Gemini 2.5 Flash**.
* **Type-Safe Data Extraction:** Uses **Pydantic Schemas** to ensure the LLM strictly returns structured JSON matching the database models (extracts exact cost, item name, and note summaries).
* **Asynchronous Backend:** Built using `python-telegram-bot` (v20+ Async) for non-blocking execution and handling multiple users concurrently.
* **Local Database Storage:** Persists transactions and notes permanently in an SQLite database using Python's built-in `sqlite3` library.
* **Environment Security:** Uses `python-dotenv` to separate sensitive credentials (API keys, bot tokens) from codebase.
* **Visual Dashboard (Planned):** An interactive web dashboard (React/Vite) to visualize expense trends and review stored notes.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** `python-telegram-bot` (Async)
* **AI Engine:** Google GenAI SDK (Gemini 2.5 Flash)
* **Data Validation:** Pydantic v2
* **Storage:** SQLite3
* **Environment Config:** python-dotenv

---

## 📂 Project Structure

```text
ai-telegram-assistant/
│
├── .env                  # Secret API keys & tokens (Git ignored)
├── .gitignore            # Tells git which files to ignore
├── requirements.txt      # Project dependencies
├── bot.py                # Bot server runner & Telegram handlers
├── ai_helper.py          # Gemini AI API wrapper & Pydantic schemas
└── db_helper.py          # SQLite database connection & CRUD operations
