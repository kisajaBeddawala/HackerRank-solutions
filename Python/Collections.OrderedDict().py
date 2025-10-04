
from collections import OrderedDict

n = int(input())
order = OrderedDict()

for i in range(n):
    inp = input().split()
    item = " ".join(inp[:-1])
    price = int(inp[-1])
    
    try:
        order[item] += price
    except KeyError:
        order[item] = price
    
for i in order:
    print(i, order[i])

