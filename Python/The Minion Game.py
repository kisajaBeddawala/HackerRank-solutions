def minion_game(string):
    # your code goes here
    stuartMark = 0
    kevinMark = 0
    length = len(string)
    vowels = "AEIOU"
   

    for i in range(length):
        if string[i] in vowels:
            #if some subtext start with a vowel letter we get all combination of it so we use (length - i)
            #for example in "BANANA" when we in index 0 which is "B" we can get total 6 combinations
            #it is equal to (length - 0) ----> ["B", "BA", "BAN", "BANA", "BANAN", "BANANA"]
            kevinMark += length - i
        else:
            stuartMark += length - i
            
    if kevinMark > stuartMark:
        print("Kevin", kevinMark)  
    elif stuartMark > kevinMark:
        print("Stuart", stuartMark)
    else:
        print("Draw")   

if __name__ == '__main__':
    s = input()
    minion_game(s)