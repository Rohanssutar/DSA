# Hashset Solution
def single_Number(nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]

if __name__ == "__main__":
     nums = [3,2,3]
     print(single_Number(nums))
        