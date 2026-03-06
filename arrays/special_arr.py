# Problem Statement
# An array is considered special if the parity of every pair of adjacent elements is different. 
# In other words, one element in each pair must be even, and the other must be odd.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

# Modulo Solution
class Solution:
    def special_Arr(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
    
if __name__ == "__main__":
    nums = [4,3,1,6]
    obj = Solution()
    print(obj.special_Arr(nums))


