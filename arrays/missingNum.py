# HashSet Solution
def missing_Num(nums: list[int]) -> int:
    hashset = set(nums)

    for i in range(len(hashset)):
        if i not in hashset:
            return i
        if i + 1 not in hashset:
            return i+1
        
if __name__ == "__main__":
    nums = [1,2,3]
    print(missing_Num(nums))

# XOR Solution
def missing_Num(nums: list[int]) -> int:
    xorr = len(nums)

    for i in range(xorr):
        xorr ^= i ^ nums[i]
    return xorr

if __name__ == "__main__":
    nums = [1,2,3]
    print(missing_Num(nums))

