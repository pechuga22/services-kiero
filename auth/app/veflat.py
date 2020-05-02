import random
import string


def random_string(str_length=30):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(str_length))