from collections import Counter

n = int(input())

data = []
for i in range(n):
    data.append(input())
    
print(len(set(data)))

c = Counter(data)
count = [count for item, count in c.items()]
print(*count, sep=' ')