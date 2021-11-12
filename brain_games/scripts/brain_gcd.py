import random
from random import randint
import prompt
from brain_games.cli import welcome_user


def get_random_value():
    value1 = random.randrange(0, 100)
    value2 = random.randrange(0, 100)
    return value1, value2


def nod(value1, value2):
    while value1 != 0 and value2 != 0:
        if value1 > value2:
            value1 = value1 % value2
        else:
            value2 = value2 % value1
    right_answer = value1 + value2
    return right_answer


def make_example(value1, value2):
    print("Question: {} {}".format(value1, value2))


def ask_user():
    user_answer = prompt.string("Your answer: ")
    return user_answer


def compare_answers(counter, user_answer, right_answer, flag=0):
    if user_answer == str(right_answer):
        print('correct')
        counter += 1
        return counter, flag
    if user_answer != str(right_answer):
        print('try again, right answer was {}'.format(right_answer))
        flag = 1
        return counter, flag


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        value1, value2 = get_random_value()
        make_example(value1,value2)
        right_answer = nod(value1, value2)
        user_answer = ask_user()
        counter, flag = compare_answers(counter, user_answer, right_answer)
        if counter == 3:
            print('Congratulations {}'.format(name))
        if flag == 1:
            break


if __name__ == '__main__':
	main()

	
