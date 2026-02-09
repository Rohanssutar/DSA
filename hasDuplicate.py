# Brute force solution
def hasDuplicate(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
        

if __name__ == "__main__":
    nums = [1,2,3,3]
    print(hasDuplicate(nums))


# Hash set solution
def hasDuplicate(nums: list[int]) -> bool:
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

if __name__ == "__main__":
    nums = [1,2,3,3]
    print(hasDuplicate(nums))