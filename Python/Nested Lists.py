if __name__ == '__main__':
    student = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append(score)
        student.append([name,score])
    
    marks.sort()
    minValue = marks[0]
    secondLowest = minValue
    for i in marks[1::]:
        if(i != minValue):
            secondLowest = i
            break
    
    student.sort()
    
    for std in student:
        if(std[1] == secondLowest):
            print(std[0])
