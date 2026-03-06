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