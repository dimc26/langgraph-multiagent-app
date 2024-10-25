import os

from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate

from assistant import config as cfg
from assistant.namespace.enum import Prompt


def load_prompt_by_name(prompt_name: str) -> str:
    filepath = os.path.join(cfg.PROMPTS_FOLDER, f"{prompt_name}.txt")

    with open(filepath) as f:
        return f.read()


def build_prompt(prompt: str) -> ChatPromptTemplate:
    system_msg = SystemMessage(
        load_prompt_by_name(f"{prompt}_system"),
        name="base",
    )

    if prompt != Prompt.DECIDER.value:
        prompt = Prompt.TASK.value

    human_msg_prompt = load_prompt_by_name(f"{prompt}_human")

    return ChatPromptTemplate(
        [system_msg, HumanMessagePromptTemplate.from_template(human_msg_prompt)],
        input_variables=["text"],
    )
