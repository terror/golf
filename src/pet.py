# https://open.kattis.com/problems/pet

print(*(lambda x: (x.index(max(x)) + 1, max(x)))([sum(list(map(int, input().split()))) for _ in range(5)]))
