class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 1
        i = 0
        digits.reverse()

        while num:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    num = 0
            else:
                digits.append(num)
                num = 0
            i += 1

        digits.reverse()
        return digits

if __name__ == "__main__":
    obj = Solution()
    num = [9,9,9]
    print(obj.plusOne(num))