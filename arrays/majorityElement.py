# Brute force solution
def majorityElement(nums: list[int]) -> int:
    n = len(nums)
    for num in nums:
        count = sum(1 for i in nums if i == num)
        if count > n // 2:
            return num
            
if __name__ == "__main__":
    nums = [5,5,5,1,1,1,5]   
    print(majorityElement(nums))


# Boyer-Moore Voting Solution
def majorityElement(nums: list[int]) -> int:
    res = count = 0

    for num in nums:
        if count == 0:
            res = num
        count += (1 if num == res else -1)
    return res

if __name__ == "__main__":
    nums = [5,5,5,1,1,1,5]
    print(majorityElement(nums))
