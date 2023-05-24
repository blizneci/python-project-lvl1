"""

This module implements Prime number game's logic.

"""

import math
import random

from brain_games.constants import RANDOM_RANGE


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_PRIME_NUMBER = 2


def is_prime(number):
    if number <= 1:
        return False
    largest_divider = int(math.sqrt(number))
    for i in range(FIRST_PRIME_NUMBER, largest_divider + 1):
        if number % i == 0:
            return False
    return True


def form_question_answer():
    number = abs(random.randrange(*RANDOM_RANGE))
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer
