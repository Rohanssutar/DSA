# Two-Pointer Solution
def reverseString(s: list[str]) -> list[str]:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return s

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(reverseString(s))
    

# Stack Solution
def reverseString(s: list[str]) -> list[str]:
    stack = []
    for c in s:
        stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1
    return s

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(reverseString(s))

