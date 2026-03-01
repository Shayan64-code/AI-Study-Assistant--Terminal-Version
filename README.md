# AI Study Assistant --Terminal Version
This AI chatbot is created as an assistant for student, It focuses and helpful in studies and code based materials.


# AI Study Assistant (CLI Version)

This is a simple command-line AI Study Assistant built using the OpenAI SDK and OpenRouter.

It works like a small chatbot inside your terminal.
You can ask it study-related questions, coding problems, or request important points for exam preparation.

The assistant remembers the conversation while the program is running.

---

## What This Project Does

* Acts as a kind and helpful study assistant
* Explains important points clearly
* Solves coding problems in an easy way
* Keeps conversation history during the session
* Stops when you type `exit`

---

## How It Works (Simple Explanation)

1. You type a question.
2. The message gets added to a `messages` list.
3. That list is sent to the model.
4. The model generates a reply.
5. The reply is printed and also saved in the list.
6. The loop continues until you type `exit`.

So basically, the program keeps sending the full conversation to the model each time so it remembers context.

---

## Project Structure

Your project likely looks like this:

```
project-folder/
│
├── app.py
├── Keys.py
├── requirements.txt
└── README.md
```

### Keys.py

This file stores your API key.

Example:

```python
KEY1 = "your_openrouter_api_key_here"
```

Important: Do NOT push this file to GitHub.
Add it to `.gitignore`.

---

## Requirements

Make sure you have Python 3.8+ installed.

Install required package:

```
pip install openai
```

---

## How to Run

Inside your project folder:

```
python app.py
```

You will see:

```
User:
```

Now start asking questions.

To stop the program, type:

```
exit
```

---

## Important Concepts Used

### 1. System Role

The system message sets the personality of the assistant:

"You are a kindful study assistant..."

This controls how the AI behaves.

---

### 2. Messages List

The `messages` list stores:

* System instruction
* User messages
* Assistant replies

This allows the model to remember previous conversation.

---

### 3. Temperature

You set:

```
temperature = 0.5
```

This makes responses balanced:

* Not too random
* Not too robotic

---

### 4. Max Tokens

```
max_tokens = 400
```

This limits how long the reply can be.

---

## Why This Is a Good Beginner Project

This project helps you understand:

* How chat completion works
* How conversation memory works
* How API requests are made
* How to handle errors
* Basic prompt control

It is a strong foundation before moving to:

* Streaming responses
* Structured outputs
* Function calling
* RAG systems
* AI agents

---

## Possible Improvements (Next Level)

You can upgrade this project by:

* Adding streaming (real-time typing effect)
* Limiting message history to avoid slow performance
* Saving chat history to a file
* Adding a simple GUI (Streamlit)
* Adding structured JSON outputs
* Adding function calling

---

## Final Note

This is a beginner-friendly AI chatbot project.
Simple, clean, and very useful for understanding how LLM chat systems work.

If you're learning AI Engineering, this is a solid starting point.

From here, you can build more advanced AI systems step by step.

Good luck with your learning and exams.
