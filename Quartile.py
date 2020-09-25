from statistics import median
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()
t=int(len(arr)/2)
if len(arr)%2==0:
    q1=arr[:t]
    q3=arr[t:]
else:
    q1=arr[:t]
    q3=arr[t+1:]
    
print(int(median(q1)))
print(int(median(arr)))
print(int(median(q3)))
