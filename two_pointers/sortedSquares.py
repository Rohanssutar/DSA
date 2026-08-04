class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        resIndex = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[resIndex] = nums[l] ** 2
                l += 1
            else:
                res[resIndex] = nums[r] ** 2
                r -= 1
            resIndex -= 1

        return res

if __name__ == "__main__":
    obj = Solution()
    nums = [-4, -1, 0, 3, 10]
    print(obj.sortedSquares(nums))