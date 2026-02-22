# Problem Statement
# You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:
#     • m is the number of valid elements in nums1,
#     • n is the number of elements in nums2.
# The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.

# Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
# You must modify nums1 in-place and do not return anything from the function.

# Three pointer Solution
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    last = m + n - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
    
    return nums1

if __name__ == "__main__":
    nums1 = [10, 20, 30, 40, 0, 0]
    m = 4
    nums2 = [1, 2]
    n = 2
    print(merge(nums1, m, nums2, n))
