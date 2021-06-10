# https://open.kattis.com/problems/speedlimit

import collections; P = collections.namedtuple('P', 's t'); v = lambda x: x if x > 0 else exit()

while True:
  (lambda x: (lambda a, b: print(f'{sum([a[i].s * b[i] for i in range(len(a))])} miles'))(x, [x[0].t] + [x[i].t - x[i - 1].t for i in range(1, len(x))]))([P(*map(int, input().split())) for _ in range(v(int(input())))])
