# https://open.kattis.com/problems/laptopsticker

print((lambda a, b, c, d: 1 if a-c >= 2 and b-d >= 2 else 0)(*map(int, input().split())))
