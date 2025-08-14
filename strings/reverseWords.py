class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        Discussion:
        O(n) time complexity as reversing the list is done one at a time
        O(n) space complexity as I created a new list of the same lenght as given string
        """
        myList = s.split()
        myList.reverse()
        return " ".join(myList)
        