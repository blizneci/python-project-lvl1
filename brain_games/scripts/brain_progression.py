#! /usr/bin/env python3

"""

This module starts brain-progression game.

"""

from brain_games import engine
from brain_games.games import progression as game


def main():
    engine.start_game(game)


if __name__ == "__main__":
    main()
