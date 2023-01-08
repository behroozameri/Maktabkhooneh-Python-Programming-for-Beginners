age = int(input())
max1 = age
max2 = max1
while age != -1 :
    age = int(input())
    if age > max1 :
        max2 = max1
        max1 = age
    elif age > max2 :
        max2 = age
print(max1,max2)
