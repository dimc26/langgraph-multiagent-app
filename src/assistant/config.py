import os

LIB_FOLDER = os.path.dirname(__file__)
PROMPTS_FOLDER = os.path.join(LIB_FOLDER, "prompts")

PARSER_MODEL = "gpt-4o-mini"
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]

AUDIO_SPEED = 1.3

APP_NAME = "Susurritos"

SHORT_LANGUAGE_OPTIONS = {"spanish": "es", "english": "en"}
LONG_LANGUAGE_OPTIONS = {"spanish": "es-ES", "english": "en-GB"}
MSG_SELECTED_LANGUAGE = LONG_LANGUAGE_OPTIONS["spanish"]
PLAY_AUDIO_SELECTED_LANGUAGE = SHORT_LANGUAGE_OPTIONS["spanish"]

LANGUAGE_MSG = {
    "unknown_value": {
        "es-ES": "No te he entendido.",
        "en-GB": "I didn't understand you."
    },
    "request_error": {
        "es-ES": "No se puede acceder al servicio de reconocimiento de voz en este momento.",
        "en-GB": "The speech recognition service cannot be accessed at this time."
    },
    "wait_timeout": {
        "es-ES": "Ha saltado un timeout.",
        "en-GB": "A timeout has occurred."
    },
    "welcome": {
        "es-ES": f"Hola, soy {APP_NAME}, ¿puedo ayudarte en algo?",
        "en-GB": f"Hi, this is {APP_NAME}, can I help you with something?"
    },
    "processing": {
        "es-ES": "Un momento por favor, estoy gestionando tu petición.",
        "en-GB": "One moment please, I am handling your request."
    },
    "more_help": {
        "es-ES": "¿Puedo ayudarte en algo más?",
        "en-GB": "Is there anything else I can help you with?"
    }
}
