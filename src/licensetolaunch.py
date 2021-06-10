# https://open.kattis.com/problems/licensetolaunch

print((lambda x: x.index(min(x)))([int(input()), list(map(int, input().split()))][1]))
