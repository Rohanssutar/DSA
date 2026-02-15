# Problem Statement
# You are given a binary array nums, return the maximum number of consecutive 1's in the array.

# Brute force solution
def consecutive_Ones(nums: list[int]) -> int:
    result = 0

    for i in range(len(nums)):
        count = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                break
            count += 1
            result = max(result, count)
    return result

if __name__ == "__main__":
    nums = [1,0,1,1,0,1]
    print(consecutive_Ones(nums))


# One Iteration Solution
def consecutive_Ones(nums: list[int]) -> int:
    result, count = 0, 0

    for num in nums:
        if num == 0:
            count = 0
        if num == 1:
            count += 1
        result = max(result, count)
    return result

if __name__ == "__main__":
    nums = [1,0,1,1,0,1]

    print(consecutive_Ones(nums))
