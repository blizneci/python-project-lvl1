#! /usr/bin/env python3

"""

This module gets game from storage and starts it.

"""

import sys
import pathlib

from brain_games import storage, engine


def main():
    script_path = pathlib.PurePath(sys.argv[0])
    script_name = script_path.name
    game_location = storage.get_game_location(script_name)
    game = storage.download_game(game_location)
    engine.start_game(game)


if __name__ == "__main__":
    main()
