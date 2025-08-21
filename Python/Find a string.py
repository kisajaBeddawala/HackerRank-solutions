def count_substring(string, sub_string):
    c = 0
    length = len(sub_string)  #get length of sub string

    # iterate through the main string
    for i in range(len(string) - length + 1):
        if (string[i:i+length] == sub_string):
            c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)