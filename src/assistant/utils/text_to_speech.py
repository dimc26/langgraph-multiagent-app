import io
import tempfile

import pygame
from gtts import gTTS


def play_answer(text: str) -> None:
    myobj = gTTS(text=text, lang="es", slow=False)

    mp3_fp = io.BytesIO()
    myobj.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_mp3:
        temp_mp3.write(mp3_fp.read())
        temp_mp3.flush()
        temp_filename = temp_mp3.name

    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
