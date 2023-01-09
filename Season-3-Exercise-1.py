inputString = input()
outputString = ''
inputString = inputString.lower()

for latter in inputString :
    if latter != 'a' and latter != 'e' and latter != 'i' and latter != 'o' and latter != 'u' :
        outputString = outputString + '.'
        outputString = outputString + latter

print(outputString)
