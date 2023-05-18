import prompt


WELCOME_MESSAGE = "Welcome to the Brain Games!"


def welcome_user() -> str:
    print(WELCOME_MESSAGE)
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
