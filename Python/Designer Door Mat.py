# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
txt = "WELCOME"
symbol = ".|."
count = 1

for i in range(n):
    if i < n//2:
        print((symbol * count).center(m,"-"))
        count += 2 
    elif i == n // 2:
        print(txt.center(m,"-"))
    else:
        count -= 2 
        print((symbol*count).center(m,"-"))
        