# Modulo Solution
class Solution:
    def special_Arr(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
    
if __name__ == "__main__":
    nums = [4,3,1,6]
    obj = Solution()
    print(obj.special_Arr(nums))

