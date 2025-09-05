k = int(input())
l = list(map(str,input().split()))

s = set(l)      #all unique room numbers 

for i in s:
    l.remove(i)     #removing one occurrence of each unique room number
    
new_s = set(l)      #in this not include captain's room number

print( "".join(list(s.symmetric_difference(new_s))))
