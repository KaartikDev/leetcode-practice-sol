class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        currInt = ""
        repitions_stack = []
        string_stack = []
        currStr = ""
        # finStr = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                currInt+=s[i]
                if s[i+1] == '[': #No malformed strings ensure this is not out of bounds
                    repitions_stack.append(int(currInt))
                    currInt = ""
            elif s[i] == "[":
                # print(string_stack,currStr)
                string_stack.append(currStr)
                currStr = ""
            elif s[i] == "]":
                # print(currStr)
                currStr = string_stack.pop() + (currStr * repitions_stack.pop())
            else:
                currStr += s[i]
        return currStr

        """
        Dicussion:
        O(n + output) --> O(n) assuming output grows proportionally
        O(n) space complexity
        """

