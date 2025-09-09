from itertools import combinations_with_replacement

txt, n = map(str,input().split())

num = int(n)

l = list(combinations_with_replacement(sorted(txt),num))

for i in l:
    print("".join(i))