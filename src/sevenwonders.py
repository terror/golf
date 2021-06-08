# https://open.kattis.com/problems/sevenwonders

import collections

print((lambda c: min(c['T'], c['G'], c['C']) * 7 + sum([c[k] ** 2 for k in c]))(collections.Counter({'T': 0, 'C': 0, 'G': 0}) + collections.Counter(input())))
