import concurrent.futures
import time
from typing import Any, Generator

import streamlit as st
from assistant import config as cfg
from assistant.main import processing
from assistant.utils.speech_to_text import parse_voice
from assistant.utils.text_to_speech import play_audio


def streaming_text(response: str) -> Generator[str, Any, None]:
    for char in response:
        yield char
        time.sleep(0.05)


st.title(cfg.APP_NAME)

if "messages" not in st.session_state:
    st.session_state.messages = []

box = st.container(height=600)

for message in st.session_state.messages:
    with box:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if not st.session_state.messages:
    with box:
        with st.chat_message("assistant"):
            welcome = cfg.LANGUAGE_MSG["welcome"][cfg.MSG_SELECTED_LANGUAGE]
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(play_audio, welcome)
                response = st.write_stream(streaming_text(welcome))
            st.session_state.messages.append({"role": "assistant", "content": response})

columns = st.columns([4, 2, 4])

while True:
    with box:
        input_status, input_text = parse_voice()

        if input_status:
            st.session_state.messages.append({"role": "user", "content": input_text})
            with st.chat_message("user"):
                st.markdown(input_text)

            response_processing = cfg.LANGUAGE_MSG["processing"][cfg.MSG_SELECTED_LANGUAGE]
            with st.chat_message("assistant"):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(play_audio, response_processing)
                    response = st.write_stream(streaming_text(response_processing))
                st.session_state.messages.append({"role": "assistant", "content": response})

            model_response = processing(input_text)
            with st.chat_message("assistant"):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(play_audio, model_response)
                    time.sleep(6)
                    response = st.write_stream(streaming_text(model_response))
            st.session_state.messages.append({"role": "assistant", "content": response})

            mensaje = cfg.LANGUAGE_MSG["more_help"][cfg.MSG_SELECTED_LANGUAGE]
            with st.chat_message("assistant"):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(play_audio, mensaje)
                    response = st.write_stream(streaming_text(mensaje))
            st.session_state.messages.append({"role": "assistant", "content": response})

        else:
            with st.chat_message("assistant"):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(play_audio, input_text)
                    response = st.write_stream(streaming_text(input_text))
            st.session_state.messages.append({"role": "assistant", "content": response})
