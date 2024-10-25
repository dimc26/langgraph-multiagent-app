import os

LIB_FOLDER = os.path.dirname(__file__)
PROMPTS_FOLDER = os.path.join(LIB_FOLDER, "prompts")

PARSER_MODEL = "gpt-4o-mini"
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]

AUDIO_SPEED = 1.3
