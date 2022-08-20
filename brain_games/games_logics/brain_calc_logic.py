import prompt
from random import randint
from random import choice


def brain_calc():
    name = prompt.string('May I have your name? ')
    print('What is the result of the expression?')
    right_answers = 0
    while right_answers != 3:
        operand_1 = randint(1, 1000)
        operand_2 = randint(1, 1000)
        operation = choice('-+*')
        print(f'Question: {operand_1} {operation} {operand_2}')
        answer = prompt.string('Your answer: ')
        if operation == '-':
            result = operand_1 - operand_2
        elif operation == '+':
            result = operand_1 + operand_2
        elif operation == '*':
            result = operand_1 * operand_2
        if answer == str(result):
            right_answers += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answers}'\n"
                  f"Let's try again, {name}!")
            right_answers = 0
            return 0
    print(f'Congratulations, {name}!')
