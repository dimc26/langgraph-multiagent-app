from enum import Enum


class Node(Enum):
    DECIDER = "decider_node"
    CORREO = "correo_node"
    CALENDARIO = "calendario_node"
    PREGUNTA = "pregunta_node"


class Graph(Enum):
    VIAJE = "viaje_node"


class ViajeNode(Enum):
    PARSER = "parser_viaje"
    FLIGHTS = "search_flights"
    BOOK = "book_hotel"
    PACKING = "packing_suggestion"
