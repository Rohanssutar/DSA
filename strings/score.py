# Problem Statement
# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# Return the score of s.

# Iteration Solution
def score(s: str) -> int:
    sum = 0
    for i in range(len(s) - 1):
        sum += abs(ord(s[i]) - ord(s[i + 1]))
    return sum

if __name__ == "__main__":
    s = "code"
    print(score(s))
