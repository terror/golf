# https://open.kattis.com/problems/shoppinglisteasy

import sys, collections, functools

(lambda n, m, d: print(*(lambda ans: (len(ans), *sorted(ans)))([k for k in d if d[k] == n]), sep="\n"))(*map(int, input().split()), (lambda l: functools.reduce(lambda x, y: x + y, [collections.Counter()] + [collections.Counter(o.split()) for o in l]))(sys.stdin.readlines()))
