n = int(input())
set1 = set(map(int,input().split()))

m = int(input())

for i in range(m):
    op = input().split()[0]
    set2 = set(map(int,input().split()))
    
    if op == "intersection_update":
        set1.intersection_update(set2)
    elif op == "update":
        set1.update(set2)
    elif op == "symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    elif op == "difference_update":
        set1.difference_update(set2)
        
print(sum(set1))