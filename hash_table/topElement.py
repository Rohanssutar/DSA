class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0 
            count[num] += 1

        sorted_num = sorted(count, key=count.get, reverse=True)
        return sorted_num[:k]

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(obj.topKFrequent(nums, k))