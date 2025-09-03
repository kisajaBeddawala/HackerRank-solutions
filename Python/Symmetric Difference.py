m = int(input())
setA = set(map(int,input().split()))
n = int(input())
setB = set(map(int,input().split()))

temp1 = setA.difference(setB)
temp2 = setB.difference(setA)

sortedList = sorted(temp1.union(temp2))

for i in sortedList:
    print(i)
