class Solution:
    def rotateArray(self, nums: list[int], k: int) -> None:
        k = k % len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        return nums

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(obj.rotateArray(nums, k))  