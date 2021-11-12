from random import randint
import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    flag = 1
    counter = 0
    while counter < 3:
        progression, lenght = generate_progression()
        random_value = get_random_value(lenght)
        right_answer = make_example(progression, random_value)
        user_answer = ask_user()
        counter, flag = compare_answer(right_answer, user_answer, counter, flag)
        if counter == 3:
            print('Congratulations {}'.format(name))
        if flag == 1:
            break


def generate_progression():
    progression = [x for x in range(randint(1, 20), randint(30, 60), randint(2, 4))]
    lenght = len(progression)
    return progression, lenght


def get_random_value(lenght):
    random_value = randint(0, lenght - 1)
    return random_value


def make_example(progression, random_value):
    print('What number is missing in the progression?')
    for index, value in enumerate(progression):
        if index == random_value:
            right_answer = value
            value = '..'
        print(value, end=' ')
    return right_answer


def ask_user():
    user_answer = prompt.string("\n Your answer: ")
    return user_answer


def compare_answer(right_answer, user_answer, counter, flag):
    if right_answer == int(user_answer):
        print('Correct!')
        counter += 1
        flag = 0
        return counter, flag
    else:
        print('Sorry, right answer was {}, try again!'.format(right_answer))
        flag = 1
        return counter, flag


if __name__ == '__main__':
    main()
