sum = 0
win = 0
for i in range(1,31):
    scoure = int(input())
    sum += scoure
    if(scoure == 3):
        win+=1
print(sum,win)
