class Solution:
    def validSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = left + ((right - left) // 2)
            sqr = mid * mid

            if sqr > num:
                right = mid - 1
            elif sqr < num:
                left = mid + 1
            else:
                return True
        return False

if __name__ == "__main__":
    num = 16
    obj= Solution()
    print(obj.validSquare(num))