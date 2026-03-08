# Problem Statement
# You are given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            j = 0
            while j < m:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == m:
                return i
        return -1
    
if __name__ == "__main__":
    haystack = "neetcodeneetcode"
    needle = "neet"
    obj = Solution()
    print(obj.strStr(haystack, needle))
