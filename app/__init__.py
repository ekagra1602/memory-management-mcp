import random

def get_random_greeting():
    """Return a random greeting from a predefined list."""
    greetings = [
        "Hello!",
        "Hi there!",
        "Greetings!",
        "Howdy!",
        "Hey!",
        "Welcome!"
    ]
    return random.choice(greetings) 