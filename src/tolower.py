# https://open.kattis.com/problems/tolower

(lambda P, T, check = lambda x: sum(list(map(lambda x: x.islower() or (x[0].isupper() and x[1:].islower()), x))) == len(x): print(sum(list(map(check, [[input() for _ in range(T)] for _ in range(P)])))))(*map(int, input().split()))
