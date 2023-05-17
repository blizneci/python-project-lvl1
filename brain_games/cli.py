import prompt


WELCOME_MESSAGE = "Welcome to the Brain Games!"


def welcome_user(message=WELCOME_MESSAGE):
    print(message)
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
