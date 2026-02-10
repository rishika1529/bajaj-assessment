from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

from app.config import OPENAI_API_KEY


llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-3.5-turbo",
    temperature=0
)

system_message = SystemMessage(
    content=(
        "You are a factual question-answering system. "
        "Reply with ONLY the correct single-word answer. "
        "No explanations. No repetition."
    )
)

prompt_template = PromptTemplate(
    input_variables=["question"],
    template="{question}"
)


def ask_ai(question: str) -> str:
    if not OPENAI_API_KEY:
        return "Unavailable"
    prompt = prompt_template.format(question=question)

    response = llm.invoke(
        [
            system_message,
            HumanMessage(content=prompt)
        ]
    )

    return response.content.strip()
