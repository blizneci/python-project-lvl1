"""

This module implements Calculator game's logic.

"""

import operator
from random import randint, choice

from brain_games.constants import (QUESTION_TEMPLATE, RANDOM_RANGE)


GAME_RULES = "What is the result of the expression?"
EXPRESSION_TEMPLATE = "{operands[0]} {operation} {operands[1]}"

OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        }


def get_expression() -> tuple:
    first_operand = randint(*RANDOM_RANGE)
    second_operand = randint(*RANDOM_RANGE)
    operation, function = choice(tuple(OPERATORS.items()))
    correct_answer = str(function(first_operand, second_operand))
    operands = [str(first_operand), str(second_operand)]
    if second_operand < 0:
        operands[1] = "({operand})".format(operand=second_operand)
    expression = EXPRESSION_TEMPLATE.format(operation=operation,
                                            operands=operands)
    return expression, correct_answer


def ask_question() -> tuple:
    expression, correct_answer = get_expression()
    question = QUESTION_TEMPLATE.format(question=expression)
    return question, correct_answer


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer.strip().lower() == correct_answer
