import speech_recognition as sr
from assistant import config as cfg


def parse_voice() -> tuple[bool, str]:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        recognized = False
        try:
            r.pause_threshold = 1.5
            r.adjust_for_ambient_noise(source)
            audio_data = r.listen(source)
            text = r.recognize_google(audio_data, language=cfg.MSG_SELECTED_LANGUAGE)
            recognized = True

        except sr.UnknownValueError:
            text = cfg.LANGUAGE_MSG["unknown_value"][cfg.MSG_SELECTED_LANGUAGE]

        except sr.RequestError:
            text = cfg.LANGUAGE_MSG["request_error"][cfg.MSG_SELECTED_LANGUAGE]

        except sr.WaitTimeoutError:
            text = cfg.LANGUAGE_MSG["request_error"][cfg.MSG_SELECTED_LANGUAGE]

    return recognized, text
