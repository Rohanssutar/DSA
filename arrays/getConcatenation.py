# Brute force (Iteration [two pass])
def getConcatenation(nums: list[int]) -> list[int]:
    ans = [] 

    for i in range(2):
        for num in nums:
            ans.append(num)
    return ans

if __name__ == "__main__":
    nums = [1,4,1,2]
    print(getConcatenation(nums))


# Iteration(One pass)
def getConcatenation(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * (2 * n)

    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans

if __name__ == "__main__":
    nums = [1,4,1,2]
    print(getConcatenation(nums))