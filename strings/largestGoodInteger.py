class solution:
    def largestGoodInteger(self, nums: str) -> str:
        res = "0"

        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                res = max(res, nums[i : i + 3])

        return "" if res == "0" else res

if __name__ == "__main__":
    obj = solution()
    nums = "6777133339"
    print(obj.largestGoodInteger(nums))