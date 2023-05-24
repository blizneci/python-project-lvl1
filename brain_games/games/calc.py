"""

This module implements Calculator game's logic.

"""

import operator
from random import randint, choice

from brain_games.constants import RANDOM_RANGE


GAME_RULES = "What is the result of the expression?"
EXPRESSION_TEMPLATE = "{first_operand} {operation} {second_operand}"

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
    expression = EXPRESSION_TEMPLATE.format(operation=operation,
                                            first_operand=first_operand,
                                            second_operand=second_operand)
    return expression, correct_answer


def ask_question() -> tuple:
    expression, correct_answer = get_expression()
    return expression, correct_answer
