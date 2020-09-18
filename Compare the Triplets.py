a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
b = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def compareTriplets(a, b):
    a1 = 0
    b1 = 0
    if(a[0] > b[0]):
        a1 += 1
    elif(a[0] < b[0]):
        b1 += 1
    else:
        a1 = a1
        b1 = b1

    if(a[1] > b[1]):
        a1 += 1
    elif(a[1] < b[1]):
        b1 += 1
    else:
        a1 = a1
        b1 = b1

    if(a[2] > b[2]):
        a1 += 1
    elif(a[2] < b[2]):
        b1 += 1
    else:
        a1 = a1
        b1 = b1

    return a1, b1


score = compareTriplets(a, b)

print(score)
