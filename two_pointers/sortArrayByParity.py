class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

if __name__ == "__main__":
    obj = Solution()
    nums = [3, 1, 2, 4]
    print(obj.sortArrayByParity(nums))