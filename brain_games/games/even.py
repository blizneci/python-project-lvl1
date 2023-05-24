"""

This module implements Even games's logic.

"""

from random import randint

from brain_games.constants import RANDOM_RANGE


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def form_question_answer() -> tuple:
    number = randint(*RANDOM_RANGE)
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer
