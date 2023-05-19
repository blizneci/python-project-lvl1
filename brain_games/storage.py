# storage.py

"""

This module implements a storage for games.

"""

from importlib import import_module


GAMES_STORAGE_PATH = "brain_games.games"

GAMES_CATALOG = {
        "brain-even": "even",
        "brain-calc": "calc",
        "brain-prime": "prime",
        "brain-gcd": "gcd",
        "brain-progression": "progression",
        }


def get_game_location(script_name: str) -> str:
    game_name = GAMES_CATALOG.get(script_name)
    game_location = ".".join((GAMES_STORAGE_PATH, game_name))
    return game_location


def download_game(game_location: str) -> str:
    game = import_module(game_location)
    return game
