location = []
maxLen = 99999999999
tempLen = 0

inputString = input()

location = inputString.split()
for i in range(0, len(location)):
    location[i] = int(location[i])

for i in range(min(location), max(location) + 1) :
    tempLen = 0
    for loc in location:
        tempLen = tempLen + abs(i - loc)
    if tempLen < maxLen :
        maxLen = tempLen

print(maxLen)
