# Problem Statement
# You are given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Brute Force Solution
class Solution:
    def num_Pairs(self, nums: list[int]) -> int:
        count = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
    
if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,1,1,3]
    print(obj.num_Pairs(nums))

# Hashmap Solution
from collections import defaultdict
class Solution:
    def num_Pairs(self, nums: list[int]) -> int:
        count = defaultdict(int)
        res = 0

        for num in nums:
            res += count[num]
            count[num] += 1
        return res

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,1,1,3]
    print(obj.num_Pairs(nums))
