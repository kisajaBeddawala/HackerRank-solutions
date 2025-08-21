if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        
        operation = input().split()
        match operation[0]:
            case "insert":
                l.insert(int(operation[1]),int(operation[2]))
                
            case "print":
                print(l)
                
            case "append":
                l.append(int(operation[1]))
                
            case "sort":
                l.sort()
                
            case "remove":
                l.remove(int(operation[1]))
                
            case "pop":
                l.pop()
                
            case "reverse":
                l.reverse()
            
            
