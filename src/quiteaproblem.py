# https://open.kattis.com/problems/quiteaproblem

import sys

print(*list(map(lambda x: "yes" if x else "no", list(map(lambda x: sum(["problem" in word.lower() for word in x]) != 0, [x.split() for x in sys.stdin.readlines()])))), sep="\n")
