class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = curSum = 0
        prefixSum = {0: 1}

        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res

if __name__ == "__main__":
    obj = Solution()
    nums, k = [2, -1, 1, 2], 2
    print(obj.subarraySum(nums, k))