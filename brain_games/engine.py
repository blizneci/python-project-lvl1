"""

This module implements game engine.

"""

from types import ModuleType

import prompt

from brain_games.cli import welcome_user


ANSWER_PROMPT = "Your answer: "
CONGRATULATIONS_TEMPLATE = 'Congratulations, {name}!'
CORRECT_ANSWER_REPLY = 'Correct!'
NUMBER_OF_ROUNDS = 3
QUESTION_TEMPLATE = "Question: {question}"
WRONG_ANSWER_TEMPLATE = '{answer!r} is wrong answer ;(. ' + \
    'Correct answer was {correct_answer!r}.\n' + \
    'Let\'s try again, {name}!'


def run(game: ModuleType) -> None:
    user_name = welcome_user()
    print(game.GAME_RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.ask_question()
        print(QUESTION_TEMPLATE.format(question=question))
        user_answer = prompt.string(ANSWER_PROMPT)
        if user_answer.strip().lower() == correct_answer:
            print(CORRECT_ANSWER_REPLY)
        else:
            print(WRONG_ANSWER_TEMPLATE.format(
                answer=user_answer,
                correct_answer=correct_answer,
                name=user_name))
            break
    else:
        print(CONGRATULATIONS_TEMPLATE.format(name=user_name))
