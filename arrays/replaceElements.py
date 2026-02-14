# In-place solution
# Time complexity: O(n), Space complexity: O(1)
def replace_Elements(nums: list[int]) -> list[int]:
    max_right = -1

    for i in range(len(nums) - 1, -1, -1):
        new_Val = max_right
        max_right = max(max_right, nums[i])
        nums[i] = new_Val
    return nums

if __name__ == "__main__":
    nums = [2,4,5,3,1,2]
    print(replace_Elements(nums))