# https://open.kattis.com/problems/jumbojavelin

print((lambda x: sum(x) - (len(x) - 1))([int(input()) for _ in range(int(input()))]))
