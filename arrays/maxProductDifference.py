class solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = 0

        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
                
        return (max1 * max2) - (min1 * min2)

if __name__ == "__main__":
    obj = solution()
    nums = [5,6,2,7,4]
    print(obj.maxProductDifference(nums))
        