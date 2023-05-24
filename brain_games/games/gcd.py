"""

This module implements GCD game's logic.

"""

import math
from random import randint, sample

from brain_games.constants import RANDOM_RANGE


RULES = "Find the greatest common divisor of given numbers."


def generate_pair_without_zero(boarders: tuple[int, int]) -> list:
    numbers = [number for number in range(*boarders) if number != 0]
    pair = sample(numbers, 2)
    return pair


def form_question_answer() -> tuple:
    pair = generate_pair_without_zero(RANDOM_RANGE)
    question = " ".join(map(str, pair))
    correct_answer = str(math.gcd(*pair))
    return question, correct_answer
