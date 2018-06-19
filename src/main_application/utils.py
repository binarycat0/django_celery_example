import random
import string

_base = string.ascii_uppercase + string.digits


def random_string(length=8):
    return ''.join(random.choice(_base) for _ in range(length))
