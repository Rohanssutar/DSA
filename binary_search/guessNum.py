# Guess API
def guess_api(pick: int):
    def guess(num: int) -> int:
        if num == pick:
            return 0
        elif num > pick:
            return -1
        else:
            return 1
    return guess

guess = guess_api(10)

# For loop Solution
def guess_Num(n: int) -> int:
    for num in range(1, n+1):
        if guess(num) == 0:
            return num

# Binary Search Solution
def guess_Num(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = left + ((right - left) // 2)
        res = guess(mid)
        if res > 0:
            left = mid + 1
        elif res < 0:
            right = mid - 1
        else:
            return mid

if __name__ == "__main__":
    n = 15
    print(guess_Num(n))
