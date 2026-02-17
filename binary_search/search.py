# Problem Statement
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in O(logn) time.

# Iterative Search Solution
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = left + ((right - left) // 2)
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1

if __name__ == "__main__":
    nums = [-1,0,2,4,6,8]
    target = 4
    print(search(nums, target)) 


# Upper bound Solution
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        middle = left + ((right - left) // 2)
        if nums[middle] > target:
            right = middle
        elif nums[middle] <= target:
            left = middle + 1
    return left - 1 if(left and nums[left - 1] == target) else -1

if __name__ == "__main__":
    nums = [-1,0,2,4,6,8]
    target = 4
    print(search(nums, target))
