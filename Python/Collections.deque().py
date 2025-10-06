from collections import deque


d = deque()
n = int(input())
for i in range(n):
    op= input().split()

    match op[0]:
        case "append":
            num = int(op[1])
            d.append(num)
        case "appendleft":
            num = int(op[1])
            d.appendleft(num)
        case "pop":
            d.pop()
        case "popleft":
            d.popleft()
    

print(*d)