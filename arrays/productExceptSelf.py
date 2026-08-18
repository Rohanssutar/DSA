class Solution:
    def productExceptSelf(self, arr: list[int]) -> list[int]:
        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,4]
    print(obj.productExceptSelf(nums))
