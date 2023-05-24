"""

This module defines project-level constants.

"""


RANDOM_RANGE = (-100, 100)
GUESS_CNT = 3
ANSWER_PROMPT = "Your answer: "
CORRECT_ANSWER_REPLY = 'Correct!'
WRONG_ANSWER_TEMPLATE = '{answer!r} is wrong answer ;(. ' + \
    'Correct answer was {correct_answer!r}.\n' + \
    'Let\'s try again, {name}!'
CONGRATULATIONS_TEMPLATE = 'Congratulations, {name}!'
