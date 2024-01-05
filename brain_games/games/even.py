from random import randint
from engine import engine
from constants import ROUNDS_COUNT, MIN, MAX

description = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0

def generate_round_data(number):
    answer = is_even(number) if "yes" else "no"

    return {'question': number, 'answer': answer}

def generate_game_data():
    data = []
    i = 1
    while i <= ROUNDS_COUNT:
        number = randint(MIN, MAX)
        data.append(generate_round_data(number))
    return data

def run(data, description):
    game_data = generate_game_data()
    engine(game_data, description)
