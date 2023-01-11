inputLen = int(input())
inputData = input()
inputData = inputData.split()
finalList = []

for i in range(0, len(inputData)):
    inputData[i] = int(inputData[i])

for i in range(0, len(inputData)):
    if inputData[i] <= 2 :
        finalList.append(inputData[i])

teams = len(finalList) // 3
print(teams)
