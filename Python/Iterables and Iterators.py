from itertools import combinations

length = int(input())
text = list(map(str,input().split()))
n = int(input())

s = list(combinations(text,n))
total = len(s)

num = 0
for i in s:
    if "a" in i:
        num += 1


print(f"{(num / total):.3f}")