# https://open.kattis.com/problems/peragrams

import collections
def main(s, d): return (lambda odd: 0 if odd == 1 and not s == s[::-1] else max(0, odd - 1))(len([d[k] for k in d if d[k] & 1]))
if __name__ == "__main__": print((lambda s: main(s, collections.Counter(s)))(list(input())))
