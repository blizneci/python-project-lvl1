"""

This module implements Even games's logic.

"""

from random import randint

from brain_games.constants import (QUESTION_TEMPLATE, RANDOM_RANGE)


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def ask_question() -> tuple:
    number = randint(*RANDOM_RANGE)
    question = QUESTION_TEMPLATE.format(question=number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.strip().lower() == correct_answer
