import random

myMin = 1
myMax = 99
hads = random.randint(myMin,myMax)
print(hads)
javab = input()
while javab != 'd' :
    if javab == 'k' :
        myMax = hads - 1
    elif javab == 'b':
        myMin = hads + 1
    hads = random.randint(myMin,myMax)
    print(hads)
    javab = input()
