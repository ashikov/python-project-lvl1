from prompt import string

def engine(game_data, description):
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print('Hello, {}!'.format(name))

    print(description)

    for round_data in game_data:
        question, answer = round_data.items()
    print()
