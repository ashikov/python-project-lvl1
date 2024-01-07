from random import randint
from brain_games.engine import engine
from brain_games.constants import ROUNDS_COUNT, MIN, MAX


def calculate(operator, number1, number2):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2


def generate_round_data(operator, number1, number2):
    answer = calculate(operator, number1, number2)

    return {
        'question': f"{number1} {operator} {number2}", 'answer': str(answer)
    }


def generate_game_data():
    operations = ['+', '-', '*']

    data = []
    i = 1
    while i <= ROUNDS_COUNT:
        random_index = randint(0, len(operations) - 1)
        operator = operations[random_index]

        number1 = randint(MIN, MAX)
        number2 = randint(MIN, MAX)

        data.append(generate_round_data(operator, number1, number2))
        i += 1
    return data


def run():
    description = 'What is the result of the expression?'
    game_data = generate_game_data()
    engine(game_data, description)
