# Gemini LLM Application

A simple Large Language Model (LLM) application built using Python and Google's Gemini API. This project allows users to interact with the Gemini model through a command-line interface and receive AI-generated responses.

## Features

- User-friendly command-line interface
- Natural language question answering
- Powered by Google's Gemini LLM
- Secure API key management using environment variables
- Simple and lightweight implementation

## Technologies Used

- Python
- Google Gemini API
- LangChain
- LangChain Google GenAI
- Python Dotenv

## Project Architecture

User Query
↓
Gemini LLM
↓
Response Generation
↓
Final Answer

## Project Structure

```text
LLM-Application/
│
├── main.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/llm_application.git
cd llm_application
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Setup API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

## Run Project

```bash
python main.py
```

## Example

Input:

```text
What is Artificial Intelligence?
```

Output:

```text
Artificial Intelligence (AI) is a branch of computer science focused on creating systems that can perform tasks requiring human intelligence such as learning, reasoning, problem-solving, and decision-making.
```

## How It Works

1. User enters a question.
2. Python sends the query to Gemini.
3. Gemini processes the request.
4. The generated response is returned to the user.

## Skills Demonstrated

- Large Language Models (LLMs)
- Prompt-based AI Applications
- API Integration
- LangChain Basics
- Environment Variable Management
- Python Development
- Git and GitHub

## What I Learned

Through this project, I gained practical experience in:

- Working with LLM APIs
- Integrating Gemini with Python
- Managing API keys securely
- Building AI-powered applications
- Understanding LLM workflows

## Future Improvements

- Chat History Support
- Streamlit Web Interface
- Voice Input and Output
- PDF Question Answering
- Retrieval-Augmented Generation (RAG)
- Multi-Model Support

## Author

Kavipriya P

Aspiring AI/ML Engineer passionate about Artificial Intelligence, Machine Learning, Deep Learning, Generative AI, and AI Agents.
