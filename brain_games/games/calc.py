"""Calculator game's logic"""

GAME_RULES = "Calculator game"


def ask_question() -> tuple:
    print("Calculator asks a question")
    return ("true", "true")


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return True
