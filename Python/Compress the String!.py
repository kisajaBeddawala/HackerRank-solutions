from itertools import groupby

txt = input()

ans = []
for k,g in groupby(txt):
    ans.append((len(list(g)), int(k)))
    
print(*ans)