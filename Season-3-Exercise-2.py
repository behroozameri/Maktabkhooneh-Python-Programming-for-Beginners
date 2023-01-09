inputString = input()
outputString = ''

count = inputString.count('1')
if count > 0 :
    for i in range (0, count - 1):
        outputString = outputString + '1'
        outputString = outputString + '+'
    outputString = outputString + '1'

count = inputString.count('2')
if count > 0 :
    outputString = outputString + '+'
    for i in range (0, count - 1):
        outputString = outputString + '2'
        outputString = outputString + '+'
    outputString = outputString + '2'

count = inputString.count('3')
if count > 0 :
    outputString = outputString + '+'
    for i in range (0, count - 1):
        outputString = outputString + '3'
        outputString = outputString + '+'
    outputString = outputString + '3'

print(outputString)
