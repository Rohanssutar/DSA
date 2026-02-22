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