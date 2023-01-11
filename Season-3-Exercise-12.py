inputLen = int(input())
myDic = dict()

for i in range(0,inputLen):
    data = input()
    data = data.split()
    myDic[data[0]] = data[1]

inputSting = input()
inputSting = inputSting.split()

outputString = ''

for item in inputSting:
    outputString = outputString + myDic.get(item, item) + ' '

outputString = outputString[:len(outputString) - 1]
print(outputString)
