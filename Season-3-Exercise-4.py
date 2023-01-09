inputString = input()
flag = 0

location_h = inputString.find('h')
if location_h != -1:
    location_e = inputString.find('e',location_h + 1)
    if location_e != -1:
        location_l1 = inputString.find('l',location_e + 1)
        if location_l1 != -1:
            location_l2 = inputString.find('l',location_l1 + 1)
            if location_l2 != -1:
                location_o = inputString.find('o',location_l2 + 1)
            else:
                flag = 1
        else:
            flag = 1
    else:
        flag = 1
else:
    flag = 1

if flag == 0 :
    print('YES')
elif flag == 1 :
    print('NO')
