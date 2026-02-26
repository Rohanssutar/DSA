# Problem Statement
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:
#     1) Every open bracket is closed by the same type of close bracket. 
#     2) Open brackets are closed in the correct order.
#     3) Every close bracket has a corresponding open bracket of the same type. 
# Return true if s is a valid string, and false otherwise.

def is_valid(s: str) -> bool:
    stack = []
    hashmap = { ")" : "(", "]" : "[", "}" : "{" }

    for c in s:
        if c in hashmap:
            if stack and stack[-1] == hashmap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False

if __name__ == "__main__":
    s = "([{}])"
    print(is_valid(s))
