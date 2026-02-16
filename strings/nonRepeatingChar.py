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