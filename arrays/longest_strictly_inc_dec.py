class Solutions:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increase = decrease = 1
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                increase = decrease = 1
            elif nums[i] > nums[i - 1]:
                increase += 1
                decrease = 1
            else:
                decrease += 1
                increase = 1
            max_length = max(max_length, increase, decrease)
        
        return max_length

if __name__ == "__main__":
    obj = Solutions()
    nums = [1,4,3,3,2]
    print(obj.longestMonotonicSubarray(nums))