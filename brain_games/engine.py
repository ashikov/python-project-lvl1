from prompt import string


def engine(game_data, description):
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print(f"Hello, {name}!")

    print(description)

    for round_data in game_data:
        question = round_data['question']
        answer = round_data['answer']

        userAnswer = string(f"Question: {question}\n")

        if userAnswer != answer:
            f"{userAnswer} is wrong answer ;(. Correct answer was {answer}. Let\'s try again, {name}!"  # noqa: E501

            return

        print('Correct!')

    print(f"Congratulations, {name}!")

    return
