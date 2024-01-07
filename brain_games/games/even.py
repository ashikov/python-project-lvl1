from random import randint
from brain_games.engine import engine
from brain_games.constants import ROUNDS_COUNT, MIN, MAX


def is_even(number):
    return number % 2 == 0


def generate_round_data(number):
    answer = "yes" if is_even(number) else "no"

    return {'question': number, 'answer': answer}


def generate_game_data():
    data = []
    i = 1
    while i <= ROUNDS_COUNT:
        number = randint(MIN, MAX)
        data.append(generate_round_data(number))
        i += 1
    return data


def run():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_data = generate_game_data()
    engine(game_data, description)
