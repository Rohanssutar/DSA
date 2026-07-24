from collections import Counter

class solution:
    def findErrorNum(self, nums: list[int]) -> list[int]:
        res = [0, 0]
        count = Counter(nums)

        for i in range(1, len(nums) + 1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i

        return res

if __name__ == "__main__":
    obj = solution()
    nums = [1,2,2,4]
    print(obj.findErrorNum(nums))