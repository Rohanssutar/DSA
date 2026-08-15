class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        res = 0

        for char in s:
            count[char] = 1 + count.get(char, 0)
            if count[char] % 2 == 0:
                res += 2

        for cnt in count.values():
            if cnt % 2:
                res += 1
                break
        return res

if __name__ == "__main__":
    obj = Solution()
    s = "abccccdd"
    print(obj.longestPalindrome(s))