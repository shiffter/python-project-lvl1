from random import randint
import prompt
from brain_games.cli import welcome_user


def get_random_value():
    return randint(0, 666)


def make_example(value):
    print("Question: {}".format(value))


def ask_user():
    user_answer = prompt.string("Your answer: ")
    return user_answer


def compare_answers(counter, user_answer, right_answer, flag=0):
    if user_answer in right_answer:
        print('Correct!')
        counter += 1
        return counter, flag
    if user_answer not in right_answer:
        flag = 1
        return counter, flag


def play_games(value):
	if value % 2 == 0:
		right_answer = ('Yes','yes')
	else:
		right_answer = ('No', 'no')
	return right_answer


def main():
	name = welcome_user()
	counter = 0
	print('Answer "Yes" if given number is even. Otherwise answer "No".')
	while counter < 3:
		value = get_random_value()
		make_example(value)
		right_answer = play_games(value)
		user_answer = ask_user()
		counter, flag = compare_answers(counter, user_answer, right_answer)
		if counter == 3:
			return ('Congratulations, {}!'.format(name))
		if flag == 1:
			print("{} is wrong answer ;(. Correct answer was {}. \nLet's try again, {}!".format(user_answer, right_answer[1], name))
			break


if __name__ == '__main__':
	main()
