from random import randint
from brain_games.engine import engine
from brain_games.constants import ROUNDS_COUNT, PROGRESSION_LENGTH, MIN, MAX


def get_progression(first_term, sequence_step, PROGRESSION_LENGTH):
    def iter(current_term, acc):
        if (len(acc) == PROGRESSION_LENGTH):
            return acc
        return iter(current_term + sequence_step, acc + [current_term])
    return iter(first_term, [])


def generate_round_data():
    first_term = randint(MIN, MAX)
    sequence_step = randint(MIN, MAX)
    progression = get_progression(first_term, sequence_step, PROGRESSION_LENGTH)
    hidden_element_index = randint(0, len(progression) - 1)
    answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(map(str, progression))

    return {
        'question': question, 'answer': str(answer)
    }


def generate_game_data():
    data = []
    i = 1
    while i <= ROUNDS_COUNT:
        data.append(generate_round_data())
        i += 1
    return data


def run():
    description = 'What number is missing in the progression?'
    game_data = generate_game_data()
    engine(game_data, description)
