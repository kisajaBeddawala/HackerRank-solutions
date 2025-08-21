def swap_case(s):
    answer = ""
    for i in s:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
            
    return answer

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)