from enum import Enum


class Prompt(Enum):
    DECIDER = "decider"
    CORREO = "correo"
    CALENDARIO = "calendario"
    PREGUNTA = "pregunta"


class Node(Enum):
    DECIDER = "decider_node"


class Graph(Enum):
    VIAJE = "viaje_subgraph"
    CORREO = "correo_subgraph"
    CALENDARIO = "calendario_subgraph"
    PREGUNTA = "pregunta_subgraph"


class ViajeNode(Enum):
    PARSER = "parser_viaje"
    FLIGHTS = "search_flights"
    BOOK = "book_hotel"
    PACKING = "packing_suggestion"
