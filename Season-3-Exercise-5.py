inputString = input()
outputString = ''
lowerLatter = 0
upperLatter = 0

for latter in inputString :
    if latter >= 'a' and latter <= 'z' :
        lowerLatter = lowerLatter + 1
    elif latter >= 'A' and latter <= 'Z' :
        upperLatter = upperLatter + 1

if upperLatter > lowerLatter :
    outputString = inputString.upper()
else:
    outputString = inputString.lower()

print(outputString)
