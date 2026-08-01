class Solution:
    def containsDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, min(n, i + k + 1)):
                if nums[i] == nums[j]:
                    return True

        return False

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(obj.containsDuplicate(nums, k))



class Solution:
    def containsDuplicate(self, nums: list[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                return True
            hashmap[nums[i]] = i

        return False

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(obj.containsDuplicate(nums, k))