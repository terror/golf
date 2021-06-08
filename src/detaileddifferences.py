# https://open.kattis.com/problems/detaileddifferences

import sys

print(*(lambda N, x: [f'{x[i]}\n{x[i + 1]}\n{"".join(["." if x[i][j] == x[i + 1][j] else "*" for j in range(len(x[i]))])[:-1]}\n' for i in range(0, len(x), 2)])(int(input()), sys.stdin.readlines()))
