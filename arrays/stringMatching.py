# Brute force solution
def string_Matching(words: list[str]) -> list[str]:
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] == words[j]:
                continue
                
            if words[i] in words[j]:
                result.append(words[i])
                break
    return result

if __name__ == "__main__":
    words = ["neetcode","neeet","neet","code"]
    print(string_Matching(words))


# Using enumerate function
def string_Matching(words: list[str]) -> list[str]:
    result = []
    for i, word in enumerate(words):
        for j, other_word in enumerate(words):
            if i != j and word in other_word:
                result.append(word)
                break
    return result

if __name__ == "__main__":
    words = ["neetcode","neeet","neet","code"]
    print(string_Matching(words))