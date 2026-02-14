# Problem Statement
# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.
# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.
# Note:
#     - The order of the elements which are not equal to val does not matter.
#     - It is not necessary to consider elements beyond the first k positions of the array.
#     - To be accepted, the first k elements of nums must contain only elements not equal to val.
# Return k as the final result.

# Brute Force Solution
def removeElement(nums: list[int], val: int) -> int:
    ans = []
    
    for num in nums:
        if num == val:
            continue
        ans.append(num)
    for i in range(len(ans)):
        nums[i] = ans[i]
    return ans

if __name__ == "__main__":
    nums = [1,1,2,3,4]
    val = 1
    print(removeElement(nums, val))


# Two Pointer Solution
def removeElement(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    nums = [1,1,2,3,4]
    val = 1
    print(removeElement(nums, val))
