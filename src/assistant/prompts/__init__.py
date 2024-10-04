import os

from assistant import config as cfg


def load_prompt_by_name(prompt_name: str) -> str:
    filepath = os.path.join(cfg.PROMPTS_FOLDER, f"{prompt_name}.txt")

    with open(filepath) as f:
        return f.read()
