class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        count = {}
        duplicate = missing = 0

        for row in grid:
            for col in row:
                count[col] = 1 + count.get(col, 0)

        for num in range(1, n * n + 1):
            if count.get(num, 0) == 0:
                missing = num
            if count.get(num, 0) == 2:
                duplicate = num

        return [duplicate, missing]

if __name__ == "__main__":
    obj = Solution()
    grid = [
        [1,3],
        [2,2]
    ]
    print(obj.findMissingAndRepeatedValues(grid))