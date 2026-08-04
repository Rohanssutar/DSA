class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i

if __name__ == "__main__":
    obj = Solution()
    g = [1,2,3]
    s = [1,1]
    print(obj.findContentChildren(g, s))