from random import randint


RULES = 'Answer "Yes" if given number is prime. Otherwise answer "No".'


def get_required_values():
    value_one = randint(1, 500)
    task = ("Question: {}".format(value_one))
    divider_count = [x for x in range(2, value_one) if value_one % x == 0]
    if len(divider_count) == 0:
        right_answer = ('yes')
    else:
        right_answer = ('no')
    return task, right_answer
