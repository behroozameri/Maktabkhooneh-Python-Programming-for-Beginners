inputString = input()
inputString = inputString.lower()

flag = 0
loc_ab = 0
loc_ba = 0

loc_ab = inputString.find('ab')
loc_ba = inputString.find('ba', loc_ab + 2)
if loc_ab != -1 and loc_ba != -1 :
    diff = loc_ab - loc_ba
    diff = abs(diff)
    if diff >= 2:
        flag = 1


if flag == 0 :
    loc_ab = 0
    loc_ba = 0

    loc_ba = inputString.find('ba')
    loc_ab = inputString.find('ab', loc_ba + 2)
    
    if loc_ab != -1 and loc_ba != -1 :
        diff = loc_ab - loc_ba
        diff = abs(diff)
        if diff >= 2:
            flag = 1


if flag == 0 :
    print('NO')
else:
    print('YES')
