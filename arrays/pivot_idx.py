# Problem Statement
# You are given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

# Brute Force Solution
class Solution:
    def pivot_Idx(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            sum_left = sum_right = 0
            for j in range(i):
                sum_left += nums[j]
            for k in range(i + 1, n):
                sum_right += nums[k]
            if sum_left == sum_right:
                return i
        return -1
    
if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    obj = Solution()
    print(obj.pivot_Idx(nums))

# Optimal Solution
class Solution:
    def pivot_Idx(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        sum_left = 0
        n = len(nums)

        for i in range(n):
            sum_right = total_sum - sum_left - nums[i] 
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
        return -1
    
if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    obj = Solution()
    print(obj.pivot_Idx(nums))