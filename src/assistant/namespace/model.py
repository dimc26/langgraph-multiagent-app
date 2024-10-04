from datetime import time
from typing import Optional as Opt

from langchain_core.pydantic_v1 import BaseModel


class CorreoItem(BaseModel):
    destinatario: str
    mensaje: str


class CalendarioItem(BaseModel):
    dia: str
    hora: time


class ViajeItem(BaseModel):
    destino: str
    fecha: str


class PreguntaItem(BaseModel):
    texto: str


class DeciderOptions(BaseModel):
    correo: bool
    calendario: bool
    viaje: bool
    pregunta: bool
