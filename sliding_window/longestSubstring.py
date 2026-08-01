class solution:
    def longestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        res = set()

        for right in range(len(s)):
            while s[right] in res:
                res.remove(s[left])
                left += 1

            length = (right - left) + 1
            longest = max(longest, length)
            res.add(s[right])

        return longest

if __name__ == "__main__":
    obj = solution()
    s = "abcabcbb"
    print(obj.longestSubstring(s)) 