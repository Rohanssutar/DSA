# Brute Force Method
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            min = 0
            for i in range(len(nums)):
                if nums[i] < nums[min]:
                    min = i
            nums[min] *= multiplier
        return nums
    
if __name__ == "__main__":
    obj = Solution()
    nums = [2,1,3,5,6]
    k = 5
    multiplier = 2
    print(obj.getFinalState(nums, k, multiplier))

# Heap Method
import heapq

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        res = nums[::]
        min_heap = []
        for i, n in enumerate(nums):
            min_heap.append((n, i))

        heapq.heapify(min_heap)

        for _ in range(k):
            num, i = heapq.heappop(min_heap)
            res[i] *= multiplier
            heapq.heappush(min_heap, (res[i], i))
        return res

if __name__ == "__main__":
    obj = Solution()
    nums = [2,1,3,5,6]
    k = 5
    multiplier = 2
    print(obj.getFinalState(nums, k, multiplier))
