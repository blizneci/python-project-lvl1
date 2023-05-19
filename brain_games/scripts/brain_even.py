#! /usr/bin/env python3

"""

This module starts brain-even game.

"""


from brain_games import engine
from brain_games.games import even as game


def main():
    engine.start_game(game)


if __name__ == "__main__":
    main()
