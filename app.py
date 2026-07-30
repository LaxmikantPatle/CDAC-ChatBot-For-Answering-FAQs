from utils import (
    clean_response,
    format_sources,
    build_prompt,
    is_greeting,
    greeting_response
)
import streamlit as st
from rag import ask_question

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CDAC Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

.stChatMessage{
    border-radius:15px;
    padding:10px;
}

.user-msg{
    background:#DCF8C6;
}

.bot-msg{
    background:#ECECEC;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image("assets/logo.png", width=170)

    st.title("CDAC Assistant")

    st.markdown("---")

    st.write("### Knowledge Base")

    st.success("Admissions")

    st.success("Courses")

    st.success("Placements")

    st.success("Fees")

    st.success("Eligibility")

    st.success("FAQs")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages=[]

        st.rerun()

# ---------------- TITLE ---------------- #

st.title("🤖 CDAC AI Assistant")

st.write(
    "Ask any question related to CDAC admissions, placements, fees, syllabus, eligibility and more."
)

# ---------------- CHAT HISTORY ---------------- #

if "messages" not in st.session_state:

    st.session_state.messages=[]

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------- USER INPUT ---------------- #

prompt=st.chat_input("Ask your question...")

if prompt:

    # Save User Message

    st.session_state.messages.append(

        {
            "role":"user",
            "content":prompt
        }

    )

    # Display User Message

    with st.chat_message("user"):

        st.markdown(prompt)

    # Assistant

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer,sources=ask_question(prompt)

        # Typing Effect

        placeholder=st.empty()

        text=""

        for word in answer.split():

            text+=word+" "

            placeholder.markdown(text+"▌")

        placeholder.markdown(text)

        # Sources

        if len(sources)>0:

            with st.expander("📄 Sources Used"):

                for src in sources:

                    st.write(src)

    # Save Assistant Message

    st.session_state.messages.append(

        {
            "role":"assistant",
            "content":answer
        }

    )

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.caption("Developed using LangChain + FAISS + Hugging Face + Streamlit")