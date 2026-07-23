class solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_ransom = {}
        map_magazine = {}

        for char in ransomNote:
            map_ransom[char] = 1 + map_ransom.get(char, 0)

        for char in magazine:
            map_magazine[char] = 1 + map_magazine.get(char, 0)

        for char, count in map_ransom.items():
            if map_magazine.get(char, 0) < count:
                return False

        return True

if __name__ == "__main__":
    obj = solution()
    ransomNote = "aa"
    magazine = "aab"
    print(obj.canConstruct(ransomNote, magazine))