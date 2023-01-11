inputLen = int(input())
nameDic = dict()

for i in range(0,inputLen):
    name = input()
    nameDic[name] = nameDic.get(name, 0) + 1

nameList = list(nameDic.keys())
nameList.sort()

for i in range(0,len(nameList)):
    print(nameList[i], nameDic[nameList[i]])
