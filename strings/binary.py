# Problem Statement
# An array is considered special if the parity of every pair of adjacent elements is different. 
# In other words, one element in each pair must be even, and the other must be odd.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

class Solution:
    def check_ones(self, s: str) -> bool:
        seen_Zero = False

        for c in s:
            if c == '0':
                seen_Zero = True
            elif seen_Zero:
                return False
        return True
    
if __name__ == "__main__":
    s = '110'
    obj = Solution()
    print(obj.check_ones(s))
