import speech_recognition as sr
from assistant.utils.text_to_speech import play_audio


def parse_voice() -> tuple[bool,str]:
    play_audio("¿En qué puedo ayudarte?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r.pause_threshold=1.5
            r.adjust_for_ambient_noise(source)
            audio_data = r.listen(source)
            text = r.recognize_google(audio_data, language="es-ES")

        except sr.UnknownValueError:
            error = "No te he entendido"
            play_audio(error)
            return False, ""
        except sr.RequestError:
            error = "No se puede acceder al servicio de reconocimiento de voz en este momento"
            play_audio(error)
            return False, error
        except sr.WaitTimeoutError:
            error = "Ha saltado un timeout"
            play_audio(error)
            return False, error

    return True, text
