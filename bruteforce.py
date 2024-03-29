import itertools
import string
import json


def simple_brute_force():
    all_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') + tuple(map(str, string.ascii_lowercase)) + tuple(map(str, string.ascii_uppercase))

    for i in range(12):
        for j in itertools.product(all_chars, repeat=i):
            yield ''.join(j)


def dictionary_brute_force():
    with open('passwords.txt') as w:
        while True:
            curr = w.readline()
            combinations = map(''.join, itertools.product(*zip(curr.upper(), curr.lower().rstrip("\n"))))
            for i in set(combinations):
                yield i


def credentials_to_json():
    dic = {"login": "a", "password": "b"}

    with open('logins.txt') as w:
       for i in range(25):
            dic.update({"login": w.readline().strip("\n"), "password": " "})
            yield json.dumps(dic)
