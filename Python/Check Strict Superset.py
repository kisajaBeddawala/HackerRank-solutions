setA = set(map(int,input().split()))
n = int(input())        #number of other sets
decisions = []          #for storing true or false regarding each set
for i in range(n):
    setB = set(map(int, input().split()))
    decisions.append(setA.issuperset(setB) and  setA != setB)  #check if setA is strict superset of setB

print(all(decisions))       #print True if all decisions are true.