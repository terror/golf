# https://open.kattis.com/problems/aaah

print((lambda x, y: ('go', 'no')[len(x) < len(y)])(input(), input()))
