# https://open.kattis.com/problems/fiftyshades

print(sum(map(lambda x: 'pink' in x.lower() or 'rose' in x.lower(), [input() for _ in range(int(input()))])) or 'I must watch Star Wars with my daughter')
