# https://open.kattis.com/problems/helpaphd

print(*(lambda x: list(map(lambda v: int(v.split('+')[0]) + int(v.split('+')[1]) if v != "P=NP" else 'skipped', x)))([input() for _ in range(int(input()))]), sep="\n")
