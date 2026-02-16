# Problem Statement
# You are given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Note: A substring is a contiguous non-empty sequence of characters within a string.

# Brute Force Solution
def length_Of_Last_Word(s: str) -> int:
    cleaned = ""
    for ch in s:
        if ch.isalnum() or ch.isspace():
            cleaned += ch 

    length = cleaned.split()
    return len(length[-1])

if __name__ == "__main__":
    s = "    fly me   to   the moon    "
    print(length_Of_Last_Word(s))


# Iteration Solution
def length_Of_Last_Word(s: str) -> int:
    i = len(s) - 1
    length = 0

    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length

if __name__ == "__main__":
    s = "    fly me   to   the moon    "
    print(length_Of_Last_Word(s))

