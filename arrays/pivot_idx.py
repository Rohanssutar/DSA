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