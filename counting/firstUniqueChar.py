class solution:
    def firstUniqueChar(self, s: str) -> int:
        map_s = {}

        for char in s:
            map_s[char] = 1 + map_s.get(char, 0)

        for char, count in enumerate(s):
            if map_s[count] == 1:
                return char
        return -1


if __name__ == "__main__":
    obj = solution()
    s = "neetcodeislove"
    print(obj.firstUniqueChar(s))