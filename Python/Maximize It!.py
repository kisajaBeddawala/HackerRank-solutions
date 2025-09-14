from itertools import product

k, m = map(int,input().split())
l = []
for i in range(k):
    elements = list(map(int,input().split()))
    n = elements[0]
    l.append([j**2 for j in elements[1:]])

#product([1,2],[3,4],[5,6]) --> (1,3,5) (1,3,6) (1,4,5) (1,4,6) (2,3,5) (2,3,6) (2,4,5) (2,4,6)
max_val = max([(sum(t)%m) for t in product(*l)])
print(max_val)
    
    
