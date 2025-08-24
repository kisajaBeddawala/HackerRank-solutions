def average(array):
    newSet = set(array)
    avg = sum(newSet) / len(newSet)
    return f"{avg:.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)