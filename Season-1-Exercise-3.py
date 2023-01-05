a = int(input())
newNum = ((a % 10) * 100) 
a = a // 10
newNum = newNum + ((a % 10) * 10)
a = a // 10
newNum = newNum + (a % 10)
numOut = newNum * 2
print(numOut)
