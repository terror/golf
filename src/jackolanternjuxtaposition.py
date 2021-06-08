# https://open.kattis.com/problems/jackolanternjuxtaposition

import functools

print(functools.reduce(lambda x, y: x * y, list(map(int, input().split()))))
