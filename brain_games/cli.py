import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def ask_username():
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    return name


def show_error_mistake(user_answer, right_answer, name):
    print("{} is wrong answer ;(. Correct answer was {}.\nLet's try again, {}!".format(user_answer, right_answer, name))


def congrats_user(name):
    print('Congratulations, {}!'.format(name))


def ask_user():
    user_answer = prompt.string("Your answer: ")
    return user_answer


def make_example(task):
    print("Question: {}".format(task))


def compare_answers(user_answer, right_answer):
    user_answer, right_answer = str(user_answer), str(right_answer)
    if user_answer.lower() == right_answer.lower():
        return True
    else:
        return False
