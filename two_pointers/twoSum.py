class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,4]
    target = 3
    print(obj.twoSum(nums, target))


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left+1, right+1]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,4]
    target = 3
    print(obj.twoSum(nums, target))