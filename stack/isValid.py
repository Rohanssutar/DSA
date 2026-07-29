# Problem Statement
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:
#     1) Every open bracket is closed by the same type of close bracket. 
#     2) Open brackets are closed in the correct order.
#     3) Every close bracket has a corresponding open bracket of the same type. 
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_parentheses = {')' : '(', ']' : '[', '}' : '{'}

        for p in s:
            if p in map_parentheses:
                if stack and stack[-1] == map_parentheses[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
                
        return True if not stack else False

if __name__ == "__main__":
    obj = Solution()
    s = "([{}])"
    print(obj.isValid(s))
