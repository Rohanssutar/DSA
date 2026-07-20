class solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j] == '0':
                return False
            
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                return False
            else:
                skip = 0
                while j < len(abbr) and abbr[j].isdigit():
                    skip = skip * 10 + int(abbr[j])
                    j += 1
                i += skip
        
        return i == len(word) and j == len(abbr)
    
if __name__ == "__main__":
    obj = solution()
    word = "apple"
    abbr = "a3e"
    print(obj.validWordAbbreviation(word, abbr))