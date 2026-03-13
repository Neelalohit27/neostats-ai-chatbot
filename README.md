# neostats-ai-chatbot
Overview

This project implements an intelligent chatbot built using Streamlit that combines Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) to provide contextual and accurate responses.

The chatbot can retrieve information from local documents using vector embeddings and FAISS vector database, and generate responses using the Groq LLM API. It also supports live web search and allows users to switch between concise and detailed response modes.

This project was developed as part of the NeoStats – Chatbot Blueprint Challenge.

Features
# 1. Retrieval-Augmented Generation (RAG)

Uses FAISS vector database to store document embeddings.

Retrieves relevant document chunks for answering queries.

Improves accuracy by providing contextual information to the LLM.

# 2. Groq LLM Integration

Uses Groq API for fast and efficient response generation.

Supports conversational interactions.

# 3. Live Web Search

Performs real-time web search when the chatbot lacks knowledge.

Ensures responses remain up-to-date.

# 4. Response Modes

Users can switch between two response styles:

Concise Mode – Short summarized answers

Detailed Mode – In-depth explanations

# 5. Modular Architecture

The project follows a clean and modular structure for maintainability and scalability.

Project Structure
project/
│

├── config/

│   └── config.py     # API keys and settings

│

├── models/

│   ├── llm.py       # LLM integration (Groq/OpenAI/Gemini)

│   └── embeddings.py   # Embedding model for RAG

│

├── utils/                   # Helper functions (RAG, web search, etc.)

│

├── app.py                   # Main Streamlit application

│

├── requirements.txt         # Required Python packages

│

└── README.md

# Technologies Used

Python

Streamlit

Groq API

FAISS Vector Database

RAG (Retrieval-Augmented Generation)

Vector Embeddings

Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
2. Install Dependencies
pip install -r requirements.txt
3. Configure API Keys
