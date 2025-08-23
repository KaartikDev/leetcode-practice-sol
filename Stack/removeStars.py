class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        #A stack is a last in first out(LIFO) structure

        stack = []

        for c in s:
            if c == '*' and len(stack) != 0:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)

        """
        Discussion:
        O(n) time complexity
        O(n) space complexity
        """