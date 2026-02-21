# Problem Statement
# You are given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above

def pascal(numrows: int) -> list[list[int]]:
    res = [[1]]

    for i in range(numrows - 1):
        temp = [0] + res[-1] + [0]
        rows = []
        for j in range(len(res[-1]) + 1):
            rows.append(temp[j] + temp[j + 1])
        res.append(rows)
        
    return res

if __name__ == "__main__":
    n = 5
    print(pascal(n))
