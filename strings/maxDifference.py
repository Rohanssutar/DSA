# Brute force solution
class solution:
    def maxDifference(self, s: str) -> int:
        odd = [] 
        even = []
        mapping = {}

        for ch in s:
            mapping[ch] = 1 + mapping.get(ch, 0)
        
        for i in mapping:
            if mapping[i] % 2 == 1:
                odd.append(mapping[i])
            else:
                even.append(mapping[i])
        
        return (max(odd) - min(even))

if __name__ == "__main__":
    obj = solution()
    s = "aaaaabbc"
    print(obj.maxDifference(s))


#Optimal Solution
class solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        odd, even = 0, len(s)

        for ch in s:
            count[ch] = 1 + count.get(ch, 0)
        
        for cnt in count.values():
            if cnt & 1:
                odd = max(odd, cnt)
            else:
                even = min(even, cnt)
        
        return (odd - even)

if __name__ == "__main__":
    obj = solution()
    s = "aaaaabbc"
    print(obj.maxDifference(s))
