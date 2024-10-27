import os

LIB_FOLDER = os.path.dirname(__file__)
PROMPTS_FOLDER = os.path.join(LIB_FOLDER, "prompts")

PARSER_MODEL = "gpt-4o-mini"
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]

AUDIO_SPEED = 1.3

APP_NAME = "Susurritos"

LANGUAGE = "english"
LANGUAGE_OPTIONS = {"spanish": "es-ES", "english": "en-GB"}
MSG_SELECTED_LANGUAGE = LANGUAGE_OPTIONS[LANGUAGE]

#Temp dict until development APIs and language functionality
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
    },
    "flights_output": {
        "es-ES": "Vuelo Syntonize con destino {destination} para {date}.",
        "en-GB": "Syntonize flight with destination {destination} for {date}."
    },
    "book_output": {
        "es-ES": "Reservado hotel Syntonize en {destination} para {date}.",
        "en-GB": "Booked Syntonize hotel in {destination} for {date}."
    },
    "packaging_output": {
        "es-ES": "Llévate una rebequita a {destination} que refresca en {date}.",
        "en-GB": "Take a jacket with you to {destination} which cools down on {date}."
    },
    "calendar_output": {
        "es-ES": "He creado un evento para el día {day} a las {hour}.",
        "en-GB": "I have created an event for {day} at {hour}."
    },
    "mail_message": {
        "es-ES": "Este es un correo escrito a partir del mensaje {message}.",
        "en-GB": "This is a mail written from the message {message}."
    },
    "mail_output": {
        "es-ES": "Le he mandado un correo a {receiver} con el siguiente mensaje {mail_message}.",
        "en-GB": "I have sent an email to {receiver} with the following message {mail_message}."
    },
}
