from collections import defaultdict

n,m = map(int,input().split())
a_list = []
d = defaultdict(list)

for i in range(n):
    d[input()].append(i+1)
    
for j in range(m):
    letter = input()
    if letter in d:
        print(*d[letter])
    else:
        print(-1)
