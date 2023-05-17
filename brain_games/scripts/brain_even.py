#! /usr/bin/env python3
from brain_games.even_game import run_even_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    run_even_game(name)


if __name__ == "__main__":
    main()
