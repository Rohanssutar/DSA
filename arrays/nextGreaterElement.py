# Problem Statement

# The next greater element of some element x in an array is the first greater element that is to the right of x in the array.
# You are given two 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2. nums2 contains unique elements.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, then the answer for this query is -1.

# Brute Force Solution
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            res.append(nums2[k])
                            found = True
                            break
                    if not found:
                        res.append(-1)  
        return res
    
if __name__ == "__main__":
    obj = Solution()
    nums1 = [4,1,2]
    nums2 = [1,2,3,4]
    print(obj.nextGreaterElement(nums1, nums2))

# Hashmap Solution
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_hashmap = {}
        res = [-1] * len(nums1)

        for i, num in enumerate(nums1):
            nums1_hashmap[num] = i
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1_hashmap:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1_hashmap[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res
    
if __name__ == "__main__":
    obj = Solution()
    nums1 = [4,1,2]
    nums2 = [1,2,3,4]
    print(obj.nextGreaterElement(nums1, nums2))