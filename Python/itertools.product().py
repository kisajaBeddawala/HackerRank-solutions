from itertools import product

s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))

l = list(product(s1,s2))

print(*l)