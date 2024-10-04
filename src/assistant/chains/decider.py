from assistant import config as cfg
from assistant.namespace.model import DeciderOptions
from assistant.prompts import load_prompt_by_name
from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


def build_decider_prompt() -> ChatPromptTemplate:
    system_msg = SystemMessage(
        load_prompt_by_name("decider_system"),
        name="base",
    )
    human_msg_prompt = load_prompt_by_name("decider_human")
    return ChatPromptTemplate(
        [system_msg, HumanMessagePromptTemplate.from_template(human_msg_prompt)],
        input_variables=["text"],
    )


def build_decider_chain() -> RunnableSerializable:
    prompt = build_decider_prompt()
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(DeciderOptions)

    return prompt | model
