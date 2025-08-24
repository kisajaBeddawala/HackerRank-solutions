def removeDuplicate(txt):
    visited = []
    newTxt = ""
    for letter in txt:
        if letter not in visited:   #if letter in visited in not add to new text
            visited.append(letter)
            newTxt += letter
    print(newTxt)
            
def merge_the_tools(string, k):
    length = len(string)
    start = 0
    end = k
    for i in range(int(length/k)):  #use to divide string in to substring
        txt = string[start:end]
        start = end             #set new start and end point 
        end += k
        removeDuplicate(txt)        #remove duplicate and print 
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)