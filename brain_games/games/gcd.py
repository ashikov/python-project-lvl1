from random import randint
from brain_games.engine import engine
from brain_games.constants import ROUNDS_COUNT, MIN, MAX


def getGcd(number1, number2):
    if number2 != 0:
        return getGcd(number2, number1 % number2)
    return number1

def generate_round_data(number1, number2):
    answer = getGcd(number1, number2)

    return {
        'question': f"{number1} {number2}", 'answer': str(answer)
    }


def generate_game_data():
    data = []
    i = 1
    while i <= ROUNDS_COUNT:
        number1 = randint(MIN, MAX)
        number2 = randint(MIN, MAX)

        data.append(generate_round_data(number1, number2))
        i += 1
    return data


def run():
    description = 'Find the greatest common divisor of given numbers.'
    game_data = generate_game_data()
    engine(game_data, description)
