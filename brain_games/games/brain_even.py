import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_required_values():
    value_one = random.randint(1, 100)
    task = ("Question: {}".format(value_one))
    if value_one % 2 == 0:
        right_answer = ('Yes')
    else:
        right_answer = ('No')
    return task, right_answer
