# Problem Statement
# You are given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

# Hashmap Solution
class Solution:
    def luckynum(self, nums: list[int]) -> int:
        hashmap = {}
        res = -1

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        for num, freq in hashmap.items():
            if num == freq:
                res = max(num, res)
        
        return res

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,2,3,3,3]
    print(obj.luckynum(nums))