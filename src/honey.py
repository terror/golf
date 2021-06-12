# https://open.kattis.com/problems/honey

print(*(lambda x: [x[int(input())] for _ in range(int(input()))])([1, 0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600]), sep="\n")
