import keyboard
import speech_recognition as sr
from assistant.utils.text_to_speech import play_answer


def parse_voice() -> tuple[bool, str]:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        r.adjust_for_ambient_noise(source)

        audio = sr.AudioData(b'', 16000, 2)

        with source as source:
            play_answer("¿En qué puedo ayudarte?")
            audio_data = []
            while not keyboard.is_pressed('q'):
                audio_chunk = r.listen(source, phrase_time_limit=1)
                audio_data.append(audio_chunk.get_raw_data())

        audio_data = b''.join(audio_data)
        audio = sr.AudioData(audio_data, source.SAMPLE_RATE, source.SAMPLE_WIDTH)

        try:
            print("Procesando...")
            text = r.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {text}")
        except sr.UnknownValueError:
            return False, "No te he entendido."
        except sr.RequestError as e:
            return False, f"Error al conectar con el servicio de reconocimiento: {e}"

    return True, text
