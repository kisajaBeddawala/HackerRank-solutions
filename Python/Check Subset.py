test = int(input())
for i in range(test):
    n1 = int(input())
    number1 = set(map(int,input().split()))
    
    n2 = int(input())
    number2 = set(map(int,input().split()))
    
    print(number1.issubset(number2))
    