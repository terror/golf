# https://open.kattis.com/problems/abc

print(*(lambda a, b: [a[i] for i in b])((lambda x: {'A': min(x), 'B': sum(x) - (max(x) + min(x)), 'C': max(x)})(list(map(int, input().split()))), input()))
