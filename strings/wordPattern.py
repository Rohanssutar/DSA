class solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res = s.split()
        map_pattern = map_s = {}

        if len(pattern) != len(res):
            return False

        for c1, c2 in zip(pattern, res):
            if c1 in map_pattern and map_pattern[c1] != c2:
                return False
            if c2 in map_s and map_s[c2] != c1:
                return False

            map_pattern[c1] = c2
            map_s[c2] = c1

        return True

if __name__ == "__main__":
    obj = solution()
    pattern = "aaa"
    s = "aa aa aa aa"
    print(obj.wordPattern(pattern, s))

