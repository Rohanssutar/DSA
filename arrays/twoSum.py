# Brute force Solution
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
if __name__ == "__main__":
    nums = [3,4,5,6]
    target = 7
    print(twoSum(nums, target))


# Hashmap (One pass) Solution
def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i

if __name__ == "__main__":
    nums = [3,4,5,6]
    target = 7
    print(twoSum(nums, target))