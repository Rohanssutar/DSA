class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return self.signFunc(product)

    def signFunc(self, product: int) -> int:
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0

if __name__ == "__main__":
    obj = Solution()
    nums = [-1,-2,-3,-4,3,2,1]
    print(obj.arraySign(nums))