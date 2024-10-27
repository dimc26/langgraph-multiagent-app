import io
import tempfile

import pygame
from assistant import config as cfg
from gtts import gTTS
from pydub import AudioSegment


def play_audio(text: str) -> None:
    myobj = gTTS(text=text, lang=cfg.MSG_SELECTED_LANGUAGE, slow=False)

    mp3_fp = io.BytesIO()
    myobj.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    audio = AudioSegment.from_file(mp3_fp, format="mp3")
    audio = audio.speedup(playback_speed=cfg.AUDIO_SPEED)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
        audio.export(temp_mp3.name, format="mp3")
        temp_filename = temp_mp3.name

    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
