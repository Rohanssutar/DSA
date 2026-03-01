# Problem Statement
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Hashmap Solution
from collections import defaultdict

def group_Anagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())

if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    print(group_Anagrams(strs))