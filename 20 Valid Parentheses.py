class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        for n in s:
            if(n == '(' or n == '[' or n == '{'):
                p.append(n)
            else:
                if(p == []):
                    return False
                else:
                    t = p.pop()
                    if(n == ')' and t != '('):
                        return False
                    elif (n == ']' and t != '['):
                        return False
                    elif (n == '}' and t != '{'):
                        return False
        return p == []

s = "()"
#s = "()[]{}"
#s = "(]"

print(Solution.isValid(Solution, s))