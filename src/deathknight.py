# https://open.kattis.com/problems/deathknight

(lambda x: print(sum(map(lambda x: "CD" not in x, x))))([input() for _ in range(int(input()))])
