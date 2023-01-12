from math import sqrt

inputLen = int(input())
inputData = []
outputData = []

for i in range(0,inputLen):
    inputData.append(int(input()))

for i in range(0,inputLen):
    outputData.append(str(sqrt(inputData[i])))
    tmp = str(float(outputData[i]) % 1)
    if len(tmp) > 6:
        intLen = int(float(outputData[i]) // 1)
        outputData[i] = str(intLen) +  str(tmp)[1:6]
    elif len(tmp) < 6:
        for j in range(len(tmp), 6):
            outputData[i] += '0'

for i in range(0,inputLen):
    print(outputData[i])
