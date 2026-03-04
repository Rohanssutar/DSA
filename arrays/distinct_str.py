# Problem Statement
# A distinct string is a string that is present only once in an array.

# You are given an array of strings arr, and an integer k, return the k-th distinct string present in arr. 
# If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

# Brute Force Solution
class Solution:
    def distinct(self, arr: list[str], k: int) -> str:
        count = 0
        res = ""

        for i in range(len(arr)):
            freq = 0
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    freq += 1
            if freq == 1:
                count += 1
                if count == k:
                    res = arr[i]
        return res
    
if __name__ == "__main__":
    arr = ["d","b","c","b","c","a"]
    k = 2
    obj = Solution()
    print(obj.distinct(arr, k))


# Hashmap Solution
class Solution:
    def distinct(self, arr: list[str], k: int) -> str:
        hashmap = {}
        count = 0
        res = ""

        for ch in arr:
            hashmap[ch] = 1 + hashmap.get(ch, 0)
        
        for ch in arr:
            if hashmap[ch] == 1:
                count += 1
                if count == k:
                    res = ch
        return res
    
if __name__ == "__main__":
    arr = ["d","b","c","b","c","a"]
    k = 2
    obj = Solution()
    print(obj.distinct(arr, k))
