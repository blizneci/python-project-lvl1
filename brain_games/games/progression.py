"""

This module implements Progression game's logic.

"""

import random

from brain_games.constants import RANDOM_RANGE


PROGRESSION_LENGTH_RANGE = (10, 15)
PROGRESSION_STEP_RANGE = (1, 10)
GAME_RULES = "What number is missing in the progression?"


def generate_progression(start: int, step: int, length: int) -> list:
    stop = start + length * step
    progression = list(range(start, stop, step))
    return progression


def ask_question():
    start = random.randint(*RANDOM_RANGE)
    step = random.randint(*PROGRESSION_STEP_RANGE)
    length = random.randint(*PROGRESSION_LENGTH_RANGE)
    progression = generate_progression(start, step, length)
    random_index = random.randrange(len(progression))
    correct_answer = str(progression[random_index])
    progression[random_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer
