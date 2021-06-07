# https://open.kattis.com/problems/shoppinglisteasy
# this is absurd
# is there a better way to do this? probably

import sys, collections, functools

def main(n, m, d): print(*(lambda ans: (len(ans), *sorted(ans)))([k for k in d if d[k] == n]), sep="\n")
if __name__ == "__main__": main(*map(int, input().split()), (lambda l: functools.reduce(lambda x, y: x + y, [collections.Counter()] + [collections.Counter(o.split()) for o in l]))(sys.stdin.readlines()))
