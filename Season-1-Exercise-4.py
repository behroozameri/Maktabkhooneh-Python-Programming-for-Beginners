number = int(input())

if number % 10 == 0 :
    newNum = number + 10
else:
    newNum = number // 10
    newNum = (newNum * 10) + 10

print(newNum)
