# Problem Statement
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

# Brute Force Solution
def prefix_Count(words: list[str], pref: str) -> int:
    count = 0

    for i in range(len(words)):
        if pref in words[i][:len(pref)]:
            count += 1
    return count

if __name__ == "__main__":
    words = ["neetcode","neet","nee","code"]
    pref = "ne"
    print(prefix_Count(words, pref))

# Built-In Method Solution
def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for i in range(len(words)):
            if words[i].startswith(pref):
                count += 1
        return count

if __name__ == "__main__":
    words = ["neetcode","neet","nee","code"]
    pref = "ne"

    print(prefix_Count(words, pref))
