# https://open.kattis.com/problems/tripletexting

from collections import Counter
print((lambda c: max(c, key=c.get))((lambda s: Counter(' '.join([s[i:i+len(list(s)) // 3] for i in range(0, len(s), len(list(s)) // 3)]).split()))(input())))
