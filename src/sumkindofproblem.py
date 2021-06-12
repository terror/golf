# https://open.kattis.com/problems/sumkindofproblem

(lambda l: print(*[" ".join([str(c), str(((n**2 + n) // 2)), str(n ** 2), str(n ** 2 + n)]) for c, n in l], sep="\n"))([map(int, input().split()) for _ in range(int(input()))])
