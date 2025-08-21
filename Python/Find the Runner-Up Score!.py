if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr)
    l.sort()
    maxValue = l[len(l)-1]
    for i in l[::-1]:
        if(i != maxValue):
            print(i)
            break