from collections import namedtuple

n = int(input())
title = input().split()
column = namedtuple('column',title)

total = 0

for i in range(n):
    inp = input().split()
    test = column(*inp)
    total += int(test.MARKS)

avg = total / n

print(avg)
