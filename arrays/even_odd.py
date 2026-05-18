arr = [1,2,3,4,5,6,7,8]

even = sum(arr[num] for num in range(len(arr)) if num % 2 == 0)
odd = sum(arr[num] for num in range(len(arr)) if num % 2 != 0)

print(even - odd)