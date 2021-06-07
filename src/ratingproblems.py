# https://open.kattis.com/problems/ratingproblems

n, k = map(int, input().split()); r = sum([int(input()) for _ in range(k)])
print(((-3*(n-k)+r) / n), ((3*(n-k)+r)/n))
