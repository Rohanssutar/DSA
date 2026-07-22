class solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answers = [set(), set()]

        for num in nums1:
            if num not in nums2:
                answers[0].add(num)
        
        for num in nums2:
            if num not in nums1:
                answers[1].add(num)
        
        return [list(answers[0]), list(answers[1])]

if __name__ == "__main__":
    obj = solution()
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    print(obj.findDifference(nums1, nums2))