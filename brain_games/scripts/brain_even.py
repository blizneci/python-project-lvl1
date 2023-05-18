#! /usr/bin/env python3
import sys
import pathlib

from brain_games.storage import get_game_location, download_game
from brain_games.engine import start_game


def main():
    script_path = pathlib.PurePath(sys.argv[0])
    script_name = script_path.name
    game_location = get_game_location(script_name)
    game = download_game(game_location)
    start_game(game)


if __name__ == "__main__":
    main()
