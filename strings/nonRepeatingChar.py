# Problem Statement
# You are given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Note: A substring is a contiguous non-empty sequence of characters within a string.

def non_Repeating_Char(s: str) -> str:
    count = {}

    for ch in s:
        count[ch] = 1 + count.get(ch, 0)
    for ch in s:
        if count[ch] == 1:
            return ch
    return '$'

if __name__ == "__main__":
    s = 'geeksforgeeks'
    print(non_Repeating_Char(s))
