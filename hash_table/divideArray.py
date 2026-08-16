class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for value in count.values():
            if value % 2:
                return False

        return True

if __name__ == "__main__":
    obj = Solution()
    nums = [3, 2, 3, 2, 2, 2]
    print(obj.divideArray(nums))