p = int(input())
s1 = set(map(int,input().split()))
q = int(input())
s2 = set(map(int,input().split()))

print(len(s1.difference(s2)))