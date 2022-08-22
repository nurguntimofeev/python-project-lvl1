import prompt
from random import randint


def is_even():
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise "no".')
    right_answers = 0
    while right_answers != 3:
        random_number = randint(1, 1000)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            result = 'yes'
        elif random_number % 2 != 0:
            result = 'no'
        if answer == result:
            right_answers += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'\n"
                  f"Let's try again, {name}!")
            right_answers = 0
            return 0
    print(f'Congratulations, {name}!')
