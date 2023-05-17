"""Even game's logic"""

from random import sample

import prompt


RANDOM_RANGE = (-100, 100)
GUESS_CNT = 3
GAME_PROMPT = 'Answer "yes" if the number is even, otherwise answer "no".'
QUESTION_TEMPLATE = 'Question: {num}\nYour answer: '
CORRECT_ANSWER_REPLY = 'Correct!'
WRONG_ANSWER_TEMPLATE = '{answer!r} is wrong answer ;(. ' + \
        'Correct answer was {correct_answer!r}.\n' + \
        'Let\'s try again, {name}!'
CONGRATULATIONS_TEMPLATE = 'Congratulations, {name}!'


def answer_question(number: int) -> str:
    answer = prompt.string(QUESTION_TEMPLATE.format(num=number))
    return answer


def is_even(number: int) -> bool:
    return number % 2 == 0


def even_to_str(number: int) -> str:
    return "yes" if is_even(number) else "no"


def get_numbers() -> dict:
    numbers = dict()
    for number in sample(range(*RANDOM_RANGE), GUESS_CNT):
        numbers[number] = even_to_str(number)
    return numbers


def run_even_game(name: str) -> None:
    numbers = get_numbers()
    print(GAME_PROMPT)
    for number, correct_answer in numbers.items():
        user_answer = answer_question(number)
        if user_answer.strip().lower() == correct_answer:
            print(CORRECT_ANSWER_REPLY)
        else:
            print(WRONG_ANSWER_TEMPLATE.format(
                answer=user_answer,
                correct_answer=correct_answer,
                name=name))
            break
    else:
        print(CONGRATULATIONS_TEMPLATE.format(name=name))
