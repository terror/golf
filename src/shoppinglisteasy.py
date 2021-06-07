# https://open.kattis.com/problems/shoppinglisteasy

import collections

def main(n, m, d):
    for _ in range(n): d += collections.Counter(list(map(str, input().split())))
    print(*(lambda ans: (len(ans), *sorted(ans)))([k for k in d if d[k] == n]), sep="\n")

if __name__ == "__main__": main(*map(int, input().split()), collections.Counter())
