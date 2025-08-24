def print_rangoli(size):
    alphabetic = "abcdefghijklmnopqrstuvwxyz"
    count = 1
    for i in range(1,size*2):
        if i <= size:    #from start to middle line (with middle line included)
            t = []
            index = size - 1
            for j in range(count):
                t.append(alphabetic[index]) #add correct letter to list
                if j < count // 2 :   #check if we are in the first half
                    index -= 1
                else:
                    index += 1
            txt = "-".join(t)       #create text with formatting using list join method
            print(txt.center(((size*2-1)*2)-1,"-"))  #get total length of text using (size*2-1)*2-1
            if i != size:               #avoid duplicate middle line
                count += 2
        else:
            count -= 2
            t = []
            index = size - 1
            for j in range(count):
                t.append(alphabetic[index]) 
                if j < count // 2 : 
                    index -= 1
                else:
                    index += 1
            print("-".join(t).center(((size*2-1)*2)-1,"-"))
                

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)