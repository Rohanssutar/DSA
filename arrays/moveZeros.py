# In-place Solution
# Time complexity: O(n), Space Complexity: O(1)
def move_Zeros(nums: list[int]) -> list[int]:
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

if __name__ == "__main__":
    nums = [1,0,0,2,0,0,5]
    print(move_Zeros(nums))