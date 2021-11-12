import random
import prompt
from brain_games.cli import welcome_user


name = welcome_user()


def main():
    flag = 0
    counter = 0
    while counter < 3:
        value_one, value_two, random_value = get_random_value()
        right_answer = make_example(random_value, value_one, value_two)
        user_answer = ask_user()
        counter, flag = compare_answers(counter, user_answer, value_one, value_two, right_answer, random_value, flag)
        if counter == 3:
            print('Congratulations, {}!'.format(name))
        if flag == 1:
            break


def get_random_value():
    value_one = random.randrange(0, 100)
    value_two = random.randrange(0, 1000)
    random_value = random.randrange(1, 4)
    return value_one, value_two, random_value


def make_example(random_value, value_one, value_two):
    if random_value == 1:
        print("Question: {} + {}".format(value_one, value_two))
        right_answer = value_one + value_two
        return right_answer
    elif random_value == 2:
        print("Question: {} - {}".format(value_one, value_two))
        right_answer = value_one - value_two
        return right_answer
    elif random_value == 3:
        print("Question: {} * {}".format(value_one, value_two))
        right_answer = value_one * value_two
        return right_answer


def ask_user():
    user_answer = prompt.string("Your answer: ")
    return user_answer


def compare_answers(counter, user_answer, value_one, value_two, right_answer, random_value, flag):
    if user_answer == str(value_one + value_two) and random_value == 1:
        print('Correct!')
        counter += 1
        return counter, flag
    elif user_answer == str(value_one - value_two) and random_value == 2:
        print('Correct!')
        counter += 1
        return counter, flag
    elif user_answer == str(value_one * value_two) and random_value == 3:
        print('Correct!')
        counter += 1
        return counter, flag
    else:
        print("{} is wrong answer ;(. Correct answer was {}. \nLet's try again, {}!".format(user_answer, right_answer, name))
        flag += 1
        return counter, flag


if __name__ == '__main__':
	main()
