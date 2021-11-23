import random
import math


RULES = 'Find the greatest common divisor of given numbers.'


def get_required_values():
    value_one, value_two = random.randint(1, 100), random.randint(1, 100)
    nod = math.gcd(value_one, value_two)
    task = ("Question: {} {}".format(value_one, value_two))
    right_answer = nod
    return task, right_answer
