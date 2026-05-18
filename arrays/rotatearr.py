arr = [1,2,3,4,5]
k = 2
res = [0] * len(arr)

for i in range(len(arr)):
    res[(i+k) % len(arr)] = arr[i]
print(res)