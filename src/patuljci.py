# https://open.kattis.com/problems/patuljci

from itertools import combinations

(lambda x: print(*list(filter(lambda y: y not in [o for o in list(set(combinations(x, 2))) if sum(x) - sum(o) == 100][0], x)), sep="\n"))([int(input()) for _ in range(9)])
