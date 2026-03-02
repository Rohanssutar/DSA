# Problem Statement
# You are given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Note: You can return the integers in any order.

# Brute force Solution
def all_Disappeared_Nums(nums: list[int]) -> list[int]:
    hashset = set(nums)
    res = []

    for i in range(1, len(nums) + 1):
        if i not in hashset:
            res.append(i)
    return res

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(all_Disappeared_Nums(nums))

# Negative marking solution
def all_Disappeared_Nums(nums: list[int]) -> list[int]:
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])

    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)
    
    return res

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(all_Disappeared_Nums(nums))
