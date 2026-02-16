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
