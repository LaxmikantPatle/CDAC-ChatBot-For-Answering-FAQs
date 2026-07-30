import re
from typing import List


# =====================================================
# Clean LLM Response
# =====================================================

def clean_response(text: str) -> str:
    """
    Clean unnecessary spaces and blank lines.
    """

    if not text:
        return "No response generated."

    text = text.replace("</s>", "")
    text = text.replace("<s>", "")

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# =====================================================
# Remove Duplicate Sources
# =====================================================

def unique_sources(sources: List[str]) -> List[str]:
    """
    Remove duplicate source names.
    """

    seen = set()
    unique = []

    for source in sources:

        if source not in seen:

            unique.append(source)

            seen.add(source)

    return unique


# =====================================================
# Format Sources
# =====================================================

def format_sources(documents):

    formatted = []

    for doc in documents:

        filename = doc.metadata.get("source", "Unknown")

        filename = filename.split("/")[-1]
        filename = filename.split("\\")[-1]

        page = doc.metadata.get("page", 0)

        formatted.append(
            f"📄 {filename} (Page {page + 1})"
        )

    return unique_sources(formatted)


# =====================================================
# Build Prompt
# =====================================================

def build_prompt(system_prompt, context, question):

    prompt = f"""
{system_prompt}

===================================

Context

{context}

===================================

Question

{question}

===================================

Answer
"""

    return prompt


# =====================================================
# Chat History
# =====================================================

def build_chat_history(messages):

    history = ""

    for msg in messages:

        role = msg["role"].capitalize()

        history += f"{role}: {msg['content']}\n"

    return history


# =====================================================
# Greeting Detection
# =====================================================

def is_greeting(text):

    greetings = [

        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening",
        "good afternoon"

    ]

    text = text.lower()

    return any(greet in text for greet in greetings)


# =====================================================
# Greeting Response
# =====================================================

def greeting_response():

    return (
        "Hello! 👋\n\n"
        "I'm your **CDAC AI Assistant**.\n\n"
        "I can answer questions related to:\n\n"
        "• Admissions\n"
        "• Courses\n"
        "• Eligibility\n"
        "• Fees\n"
        "• Placements\n"
        "• Syllabus\n"
        "• FAQs\n\n"
        "Ask me anything!"
    )


# =====================================================
# Out-of-Scope Response
# =====================================================

def outside_scope():

    return (
        "I'm designed to answer questions only "
        "from the CDAC documents available in my "
        "knowledge base."
    )


# =====================================================
# Response Statistics
# =====================================================

def response_stats(answer):

    words = len(answer.split())

    chars = len(answer)

    return {

        "words": words,

        "characters": chars

    }