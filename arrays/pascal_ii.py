class Solution:
    def pascal_ii(self, row_index: int) -> list[int]:
        res = [[1]]

        for i in range(row_index):
            temp = [0] + res[-1] + [0]
            rows = []
            for j in range(len(res[-1]) +  1):
                rows.append(temp[j] + temp[j + 1])
            res.append(rows)

        return res[row_index]

if __name__ == "__main__":
    obj = Solution()
    n = 3
    print(obj.pascal_ii(n))