import random
import operator
from brain_games.cli import welcome_user

RULES = 'What is the result of the expression?'


def get_required_values():
	value_one = random.randint(1,100)
	value_two = random.randint(1,100)
	diction = {'*': operator.mul, '-': operator.sub, '+': operator.add}
	description_operation, random_operation = random.choice(list(diction.items()))
	task = ("Question: {} {} {}".format(value_one, description_operation, value_two))
	right_answer = random_operation(value_one, value_two)
	return task, right_answer


