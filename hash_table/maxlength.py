class solution:
    def maxlengthsubstring(self, s: str) -> int:
        map_char = {}
        res = -1

        for i, c in enumerate(s):
            if c in map_char:
                res = max(res, i - map_char[c] - 1)
            else:
                map_char[c] = i

        return res

if __name__ == "__main__":
    obj = solution()
    s = "abca"
    print(obj.maxlengthsubstring(s))
