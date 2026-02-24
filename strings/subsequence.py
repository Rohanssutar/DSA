# Two-pointer solution
def is_Subsequence(s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return True if i == len(s) else False

if __name__ == "__main__":
    s = "node"
    t = "neetcode"
    print(is_Subsequence(s, t))