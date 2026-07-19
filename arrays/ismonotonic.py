class solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increase, decrease = True, True

        for i in range(len(nums) - 1):
            if not nums[i] <= nums[i + 1]:
                increase = False
            if not nums[i] >= nums[i + 1]:
                decrease = False
        
        return increase or decrease
    
if __name__ == "__main__":
    obj = solution()
    nums = [1,3,2]
    print(obj.isMonotonic(nums))