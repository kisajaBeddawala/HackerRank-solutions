from itertools import permutations

txt, n = map(str,input().split())

num = int(n)

l = list(permutations(txt,num))
l.sort()

for i in l:
    print("".join(i)) 