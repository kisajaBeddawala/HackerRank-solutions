n = int(input())
s = set(map(int, input().split()))

q = int(input())

for i in range(q):
    query = input().split()
    match query[0]:
        case "pop":
            s.pop()
        case "remove":
            s.remove(int(query[1]))
        case "discard":
            s.discard(int(query[1]))

print(sum(s))
