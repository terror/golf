# https://open.kattis.com/problems/ratingproblems

import sys; print(*(lambda n, k, r: [(-3*(n-k)+r) / n, (3*(n-k)+r)/n])(*map(int, input().split()), sum([int(x) for x in sys.stdin.readlines()])))
