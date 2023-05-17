import prompt


WELCOME_MESSAGE = "Welcome to the Brain Games!"


def welcome_user(message: str = WELCOME_MESSAGE) -> str:
    print(message)
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
