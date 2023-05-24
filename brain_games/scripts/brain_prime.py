#! /usr/bin/env python3

"""

This module starts brain-prime game.

"""

from brain_games import engine
from brain_games.games import prime as game


def main():
    engine.run(game)


if __name__ == "__main__":
    main()
