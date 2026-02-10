# Brute Force Solution
def removeElement(nums: list[int], val: int) -> int:
    ans = []

    for num in nums:
        if num == val:
            continue
        ans.append(num)
    for i in range(len(ans)):
        nums[i] = ans[i]
    return ans

if __name__ == "__main__":
    nums = [1,1,2,3,4]
    val = 1
    print(removeElement(nums, val))


# Two Pointer Solution
def removeElement(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    nums = [1,1,2,3,4]
    val = 1
    print(removeElement(nums, val))