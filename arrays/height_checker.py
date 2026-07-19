class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        occurrences = [0] * 101
        for height in heights:
            occurrences[height] += 1
        
        expected = []
        for height in range(1, 101):
            c = occurrences[height]
            for _ in range(c):
                expected.append(height)
        
        result = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1
        
        return result
    
if __name__ == "__main__":
    obj = Solution()
    heights = [1, 1, 4, 2, 1, 3]
    print(obj.heightChecker(heights))
