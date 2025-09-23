class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        
        openP = set(['(','{','['])
        

        for c in s:
            print(parenStack)
            if c in openP:
                parenStack.append(c)
            else:
                if len(parenStack) == 0: #no matching open exists
                    return False
                matchingParen = parenStack.pop()
                if c == ')' and  matchingParen != '(': #wrong types of matching
                    return False
                if c == '}' and matchingParen != '{':
                    return False
                if c == ']' and matchingParen != '[':
                    return False
        
        return len(parenStack) == 0

