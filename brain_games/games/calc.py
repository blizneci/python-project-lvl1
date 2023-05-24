"""

This module implements Calculator game's logic.

"""

import operator
from random import choice, sample
from typing import Callable

from brain_games.constants import RANDOM_RANGE


RULES = "What is the result of the expression?"
EXPRESSION_TEMPLATE = "{first_operand} {operation} {second_operand}"

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def generate_answer(operands: list[int],
                    func: Callable[[int, int], int]) -> str:
    first_operand, second_operand = operands
    answer = func(first_operand, second_operand)
    return str(answer)


def generate_expression(operands: list[int], operation: str) -> str:
    first_operand, second_operand = operands
    expression = EXPRESSION_TEMPLATE.format(operation=operation,
                                            first_operand=first_operand,
                                            second_operand=second_operand)
    return expression


def form_question_answer() -> tuple[str, str]:
    operands = sample(range(*RANDOM_RANGE), 2)
    operation, function = choice(tuple(OPERATORS.items()))
    expression = generate_expression(operands, operation)
    correct_answer = generate_answer(operands, function)
    return expression, correct_answer
