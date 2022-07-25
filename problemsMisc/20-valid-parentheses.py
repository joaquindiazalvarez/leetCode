class Solution:
    def isValid(self, s: str) -> bool:
        current = []
        for character in s:
        #caso 1 si es (
            if character == '(':
                current.append('openround')
        #caso 2 si es [
            elif character == '[':
                current.append('opensquare')
        #caso 3 si es {
            elif character == '{':
                current.append('openbraces')
            elif character == ')' and 'openround' in current:
                if current[-1] == 'openround':    
                    current.pop()
                else:
                    return False
            elif character == ']' and 'opensquare' in current:
                if current[-1] == 'opensquare':
                    current.pop()
                else:
                    return False
            elif character == '}' and 'openbraces' in current:
                if current[-1] == 'openbraces':
                    current.pop()
                else:
                    return False
            else:
                return False
        if len(current) == 0:
            return True
        else:
            return False

obj1 = Solution()
print(obj1.isValid('()'))
print(obj1.isValid("()[]{}"))
print(obj1.isValid("(]"))





               