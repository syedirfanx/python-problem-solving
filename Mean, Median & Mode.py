import collections
import statistics

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

mean = sum(arr)/len(arr)

print(mean)

arr.sort()


print(statistics.median(arr))

data = collections.Counter(arr)
data_list = dict(data)


max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(arr):
    print(arr[0])
else:
    mode_val.sort()
    print(mode_val[0])
