for i in range (0, 10):
    inputString = input()
    outputString = inputString.lower()
    outputString = outputString[0].upper() + outputString[1:]
    print(outputString)
