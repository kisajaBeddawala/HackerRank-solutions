from collections import Counter

n = int(input())
shoes = list(map(int,input().split()))
shoes_counter = dict(Counter(shoes).items())  #convert to dict for easy access
c = int(input())

total = 0
for i in range(c):
    size, price = map(int,input().split())
    
    if size in  shoes_counter:  #check if size is available otherwise get keyerror
        if shoes_counter[size] > 0:
            total += price
            shoes_counter[size] -= 1
    
print(total)

    
    