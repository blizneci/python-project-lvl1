"""

This module implements GCD game's logic.

"""

import math
from random import randint, sample

from brain_games.constants import RANDOM_RANGE


GAME_RULES = "Find the greatest common divisor of given numbers."


def get_pair() -> list:
    pair = sample(range(*RANDOM_RANGE), 2)
    if 0 in pair:
        zero_index = pair.index(0)
        pair[zero_index] = randint(range(1, RANDOM_RANGE[1]))
    return pair


def ask_question() -> tuple:
    pair = get_pair()
    question = " ".join(map(str, pair))
    correct_answer = str(math.gcd(*pair))
    return question, correct_answer
