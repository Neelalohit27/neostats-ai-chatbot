
import streamlit as st
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.llm import get_chatgroq_model
from models.embeddings import load_vectorstore
from utils.retriever import retrieve_context


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="NeoStats AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False


# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.title("⚙ Settings")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_started = True
        st.rerun()

    st.divider()

    theme_toggle = st.toggle(
        "🌙 Dark Mode",
        value=True if st.session_state.theme == "dark" else False
    )

    if theme_toggle:
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"

    mode = st.radio(
        "Response Mode",
        ["Concise", "Detailed"]
    )

    st.divider()

    st.caption("Model")
    st.write("Groq - LLaMA3")

    st.caption("Features")
    st.write("RAG + Web Search")


# ------------------------------------------------
# THEME COLORS
# ------------------------------------------------

if st.session_state.theme == "dark":

    bg_color = "#0f172a"
    text_color = "#ffffff"
    bot_color = "#1e293b"
    user_color = "#2563eb"

else:

    bg_color = "#f9fafb"
    text_color = "#111827"
    bot_color = "#e5e7eb"
    user_color = "#2563eb"


# ------------------------------------------------
# CSS
# ------------------------------------------------

st.markdown(f"""
<style>

.stApp {{
background-color:{bg_color};
color:{text_color};
}}

.chat-header {{
text-align:center;
font-size:42px;
font-weight:bold;
background: linear-gradient(90deg,#6366f1,#22c55e);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}}

.sub-header {{
text-align:center;
color:gray;
margin-bottom:40px;
}}

.user-bubble {{
background:{user_color};
color:white;
padding:12px 16px;
border-radius:16px;
margin-bottom:10px;
animation: fadeIn .3s ease;
}}

.bot-bubble {{
background:{bot_color};
padding:12px 16px;
border-radius:16px;
margin-bottom:10px;
animation: fadeIn .3s ease;
}}

@keyframes fadeIn {{
from {{opacity:0; transform:translateY(10px)}}
to {{opacity:1; transform:translateY(0)}}
}}

.center-screen {{
text-align:center;
padding-top:120px;
}}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.markdown(
'<div class="chat-header">NeoStats AI Assistant</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="sub-header">LangChain • Groq • RAG Powered Chatbot</div>',
unsafe_allow_html=True
)


# ------------------------------------------------
# LOAD MODELS
# ------------------------------------------------

@st.cache_resource
def get_vectorstore():
    return load_vectorstore()

@st.cache_resource
def get_model():
    return get_chatgroq_model()

vectorstore = get_vectorstore()
chat_model = get_model()


# ------------------------------------------------
# START SCREEN
# ------------------------------------------------

if not st.session_state.chat_started:

    st.markdown('<div class="center-screen">', unsafe_allow_html=True)

    st.markdown("### Welcome to NeoStats AI Assistant")
    st.markdown("Ask questions, analyze documents, or search the web.")

    if st.button("🚀 Start New Chat"):
        st.session_state.chat_started = True
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()


# ------------------------------------------------
# DISPLAY CHAT
# ------------------------------------------------

for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f'<div class="user-bubble">{message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="bot-bubble">{message["content"]}</div>',
            unsafe_allow_html=True
        )


# ------------------------------------------------
# CHAT INPUT
# ------------------------------------------------

prompt = st.chat_input("Message NeoStats AI...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    st.markdown(
        f'<div class="user-bubble">{prompt}</div>',
        unsafe_allow_html=True
    )

    with st.spinner("Thinking..."):

        context = retrieve_context(prompt, vectorstore)

        if mode == "Concise":
            instruction = "Answer briefly in 2-3 lines."
        else:
            instruction = "Provide a detailed explanation."

        final_prompt = f"""
You are a helpful AI assistant.

Context:
{context}

Question:
{prompt}

Instruction:
{instruction}
"""

        response = chat_model.invoke(final_prompt)
        answer = response.content


    placeholder = st.empty()
    typed = ""

    for char in answer:
        typed += char
        placeholder.markdown(
            f'<div class="bot-bubble">{typed}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.01)

    st.session_state.messages.append({"role": "assistant", "content": answer})
