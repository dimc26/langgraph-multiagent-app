import speech_recognition as sr
from assistant.utils.text_to_speech import play_answer


def parse_voice() -> tuple[bool,str]:
    play_answer("¿En qué puedo ayudarte?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r.pause_threshold=1.5
            r.adjust_for_ambient_noise(source)
            audio_data = r.listen(source)
            text = r.recognize_google(audio_data, language="es-ES")
            print(text)
        except sr.UnknownValueError:
            error = "No te he entendido"
            play_answer(error)
            return False, ""
        except sr.RequestError as e:
            error = "No se puede acceder al servicio de reconocimiento de voz en este momento"
            play_answer(error)
            return False, error
        except sr.WaitTimeoutError:
            error = "Ha saltado un timeout"
            play_answer(error)
            return False, error

    return True, text
