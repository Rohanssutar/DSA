class solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[l] = nums[i]
                l += 1
        return l


if __name__ == "__main__":
    obj = solution()
    nums = [1,1,2,3,4]
    print(obj.removeDuplicates(nums))