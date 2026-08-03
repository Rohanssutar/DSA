class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map_s, map_t = {}, {}

        for i, ch in enumerate(s):
            map_s[ch] = 1 + map_s.get(ch, 0)

        for i, ch in enumerate(t):
            map_t[ch] = 1 + map_t.get(ch, 0)

        for ch in map_t:
            if ch not in map_s or map_s[ch] < map_t[ch]:
                return ch

        return ""

if __name__ == "__main__":
    obj = Solution()
    s = "abcd"
    t = "abcde"
    print(obj.findTheDifference(s, t))