from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        count = Counter(words[0])

        for word in words:
            curr_count = Counter(word)
            for char in count:
                count[char] = min(count[char], curr_count[char])

        res = []
        for char in count:
            for _ in range(count[char]):
                res.append(char)
        return res

if __name__ == "__main__":
    obj = Solution()
    words = ["bella", "label", "roller"]
    print(obj.commonChars(words)) 