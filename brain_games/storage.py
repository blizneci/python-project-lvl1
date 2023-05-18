from importlib import import_module


GAMES_STORAGE_PATH = "brain_games.games"

games_catalog = {
        "brain-even": "even",
        "brain-calc": "calc",
        }


def get_game_location(script_name: str) -> str:
    game_name = games_catalog.get(script_name)
    game_location = ".".join((GAMES_STORAGE_PATH, game_name))
    return game_location


def download_game(game_location: str) -> str:
    game = import_module(game_location)
    return game
