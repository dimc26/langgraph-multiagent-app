from enum import Enum


class Prompt(Enum):
    DECIDER = "decider"
    MAIL = "mail"
    CALENDAR = "calendar"
    QUESTION = "question"
    TRAVEL = "travel"


class Node(Enum):
    DECIDER = "decider_node"


class Graph(Enum):
    TRAVEL = "travel_graph"
    MAIL = "mail_graph"
    CALENDAR = "calendar_graph"
    QUESTION = "question_graph"


class TravelNode(Enum):
    PARSER = "parser_travel_node"
    FLIGHTS = "search_flights_node"
    BOOK = "book_hotel_node"
    PACKING = "packing_suggestion_node"


class QuestionNode(Enum):
    PARSER = "parser_question_node"
    SEARCH = "search_answer_node"

class MailNode(Enum):
    PARSER = "parser_mail_node"
    WRITE = "write_mail_node"
    SEND = "send_mail_node"

class CalendarNode(Enum):
    PARSER = "parser_calendar_node"
    EVENT = "set_event_node"
