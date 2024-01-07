from random import randint
from brain_games.engine import engine
from brain_games.constants import ROUNDS_COUNT, MIN, MAX
from math import sqrt


def is_prime(number):
    if number <= 1:
        return False

    divisor = 2
    while divisor <= sqrt(number):
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def generate_round_data(number):
    answer = "yes" if is_prime(number) else "no"

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
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501
    game_data = generate_game_data()
    engine(game_data, description)
