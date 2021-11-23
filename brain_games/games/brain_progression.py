from random import randint
import random


RULES = 'What number is missing in the progression?'


def get_required_values():
    random_progression = [x for x in range(randint(1, 5), randint(15, 25), randint(2, 3))]
    secret_value = random.choice(random_progression)
    secret_progression = []
    for index, value in enumerate(random_progression):
        secret_progression.append(value)
        if value == secret_value:
            secret_progression[index] = '..'
    task = "Question: {}".format(' '.join(map(str, secret_progression)))
    right_answer = secret_value
    return task, right_answer
