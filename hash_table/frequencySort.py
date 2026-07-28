from collections import Counter

class solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        map_nums = Counter(nums)
        nums.sort(key=lambda n : (map_nums[n], -n))
        return nums

if __name__ == "__main__":
    obj = solution()
    nums = [1,1,2,2,2,3]
    print(obj.frequencySort(nums))