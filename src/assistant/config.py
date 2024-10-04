import os

LIB_FOLDER = os.path.dirname(__file__)
PROMPTS_FOLDER = os.path.join(LIB_FOLDER, "prompts")

PARSER_MODEL = "gpt-4o-mini"

AZURE_OPENAI_DEPLOYMENT = {
    "gpt-4o": "cog-gpt4o-01",
    "gpt-4o-mini": "cog-gpt4o-mini-01",
}[PARSER_MODEL]
