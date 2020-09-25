import math
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

mean = sum(arr)/len(arr)

sum = 0

for i in range(n):
    sum += (arr[i]-mean)**2

sd = math.sqrt(sum/n)

print("%0.1f"%sd)