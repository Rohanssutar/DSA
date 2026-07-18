# Brute Force Solution
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curSum = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[j - 1]:
                    break
                curSum += nums[j]
            res = max(res, curSum)
        return res
    
if __name__ == "__main__":
    nums = [10,20,30,5,10,50]
    obj = Solution()
    print(obj.maxAscendingSum(nums))


# Optimal Solution
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = curSum= nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curSum = 0

            curSum += nums[i]
            res = max(res, curSum)

        return res

if __name__ == "__main__":
    nums = [10,20,30,5,10,50]
    obj = Solution()
    print(obj.maxAscendingSum(nums))


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum

if __name__ == "__main__":
    nums = [10,20,30,5,10,50]
    obj = Solution()
    print(obj.maxAscendingSum(nums))