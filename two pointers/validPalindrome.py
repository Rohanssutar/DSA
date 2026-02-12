# Two-pointer solution
def valid_Palindrom(s: str) -> bool:
    left, right = 0, len(s) -1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while right > left and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            skipL, skipR = s[left + 1:right + 1], s[left:right]
            return (skipL == skipL[::-1] or skipR == skipR[::-1])
        left, right = left + 1, right - 1
    return True

if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    print(valid_Palindrom(s))