# https://open.kattis.com/problems/peragrams

import collections

print((lambda s: (lambda odd: 0 if odd == 1 and not s == s[::-1] else max(0, odd - 1))(len(list(filter(lambda x: x & 1, collections.Counter(s).values())))))(list(input())))
