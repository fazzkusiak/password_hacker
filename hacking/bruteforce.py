import itertools
import string


def guess_password():
    letters = string.ascii_lowercase
    all_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') + tuple(map(str, string.ascii_lowercase))
    for i in range(4):
        for j in itertools.product(all_chars, repeat=i):
            yield ''.join(j)

func = guess_password()
