class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            for col in row:
                if col == target:
                    return True
        return False

if __name__ == "__main__":
    obj = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    print(obj.searchMatrix(matrix, target))