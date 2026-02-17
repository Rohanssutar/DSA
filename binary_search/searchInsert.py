# Brute Force Solution (Binary Search)
def search_Insert(nums: list[int], target: int) -> int:
    if target not in nums:
        nums.append(target)
        nums.sort()
    
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + ((right- left) // 2)
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] == target:
            left = middle + 1
        else:
            return middle
        
if __name__ == "__main__":
    nums = [-1,0,2,4,6,8]
    target = 5
    print(search_Insert(nums, target))


# Binary Search Solution
def search_Insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + ((right- left) // 2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return left

if __name__ == "__main__":
    nums = [-1,0,2,4,6,8]
    target = 5
    print(search_Insert(nums, target))


# Linear Search Solution
def search_Insert(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

if __name__ == "__main__":
    nums = [-1,0,2,4,6,8]
    target = 5
    print(search_Insert(nums, target))