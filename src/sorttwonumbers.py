# https://open.kattis.com/problems/sorttwonumbers

print(*(lambda x: sorted(x))(list(map(int, input().split()))))
