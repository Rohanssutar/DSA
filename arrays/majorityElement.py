def majorityElement(nums: list[int]) -> int:
    n = len(nums)
    for num in nums:
        count = 0
        for i in nums:
            if i == num:
                count += 1
            return num
            
if __name__ == "__main__":
    nums = [5,5,5,1,1,1,5]   
    print(majorityElement(nums))