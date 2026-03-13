import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq model name
