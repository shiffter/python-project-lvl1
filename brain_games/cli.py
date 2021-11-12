import prompt


def welcome_user():
	print("Welcome to brain games!")
	name = prompt.string('May I have your name? ')
	print('Hello, {}!'.format(name))
	return name
