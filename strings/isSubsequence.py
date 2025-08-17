class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Length check
        if len(s) > len(t):
            return False
        #Empty subsequence check
        if len(s) == 0:
            return True



        # Simple traversal of long string, count the number of chacacters
        foundCount = 0
        for i in range(len(t)):
            if t[i] == s[foundCount]:
                foundCount+=1
                if (foundCount==len(s)):
                    return True
        return False

        """
        Discussion:
        O(n) time complexity
        O(1) space complexity
        """


        