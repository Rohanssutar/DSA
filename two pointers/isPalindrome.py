# Problem Statement
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Reverse String Solution
def is_Palindrome(s: str) -> bool:
    new_str = ''
    for char in s:
        if char.isalnum():
            new_str += char.lower()
    return new_str == new_str[::-1]

if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    print(is_Palindrome(s))


# Two-pointer solution
def is_Palindrome(s : str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while right > left and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        
        left, right = left + 1, right - 1
    return True

if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    print(is_Palindrome(s))


