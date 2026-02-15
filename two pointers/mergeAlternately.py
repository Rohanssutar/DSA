# Problem Statement
# You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process.
# If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.
# Return the final merged string.

# Two pointer solution 1
def mergeAlternatively(word1: str, word2: str) -> str:
    i, j = 0, 0
    res = []
    while (i < len(word1)) and (j < len(word2)):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])
    return "".join(res)

if __name__ == "__main__":
    word1 = "ab"
    word2 = "uvwxyz"
    print(mergeAlternatively(word1, word2))


# Two pointer solution 2
def mergeAlternatively(word1: str, word2: str) -> str:
    n, m = len(word1), len(word2)
    i, j = 0, 0
    res = []
    while (i < n) or (j < m):
        if i < n:
            res.append(word1[i])
        if j < m:
            res.append(word2[j])
        i += 1
        j += 1
    return "".join(res)

if __name__ == "__main__":
    word1 = "ab"
    word2 = "uvwxyz"

    print(mergeAlternatively(word1, word2))
