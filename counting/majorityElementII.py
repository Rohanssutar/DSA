class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        count = {}
        res = []

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for num, freq in count.items():
            if freq > (n // 3):
                res.append(num)

        return res

if __name__ == "__main__":
    obj = Solution()
    nums = [5,2,3,2,2,2,2,5,5,5]
    print(obj.majorityElement(nums))
