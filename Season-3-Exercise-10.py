def changeDataType(a) :
    data = a.split()
    for i in range(0, len(data)):
        data[i] = int(data[i])
    return data

#---------------------------------------------
flag = 0
inputData = []
inputLen = int(input())
inputData.append(changeDataType(input()))

for i in range(1, inputLen):
    inputData.append(changeDataType(input()))

for i in range(0, inputLen) :
    for j in range(0, inputLen) :
        a = inputData[i]
        b = inputData[j]
        if a[0] < b[0] and a[1] > b[1]:
            flag = 1
            break

if flag == 1:    
    print('happy irsa')
else:
    print('poor irsa')
