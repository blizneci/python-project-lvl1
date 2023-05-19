"""

This module implements game engine.

"""

from types import ModuleType

import prompt

from brain_games.cli import welcome_user
from brain_games.constants import GUESS_CNT
from brain_games.constants import (CORRECT_ANSWER_REPLY, WRONG_ANSWER_TEMPLATE,
                                   CONGRATULATIONS_TEMPLATE, ANSWER_PROMPT)


def start_game(game: ModuleType) -> None:
    user_name = welcome_user()
    print(game.GAME_RULES)
    for _ in range(GUESS_CNT):
        question, correct_answer = game.ask_question()
        print(question)
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
