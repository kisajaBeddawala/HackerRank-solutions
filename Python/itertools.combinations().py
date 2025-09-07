from itertools import combinations

txt, n = map(str,input().split())

num = int(n)

for i in range(1,num+1):
    l = list(combinations(sorted(txt),i))  #if the input iterable is sorted, the combination tuples will be produced in sorted order.
    for j in l:
        print("".join(j))