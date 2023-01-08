def findCount(number):
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count+=1
    return count

maxNumber = 0
maxCount = 0
for i in range(1,21):
    num = int(input())
    mycount = findCount(num)
    if mycount > maxCount:
        maxCount = mycount
        maxNumber = num
    elif mycount == maxCount:
        if maxNumber < num :
            maxNumber = num
print(maxNumber,maxCount)
