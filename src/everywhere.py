# https://open.kattis.com/problems/everywhere

print(*(lambda n: [len(set([input() for _ in range(int(input()))])) for _ in range(n)])(int(input())), sep="\n")
