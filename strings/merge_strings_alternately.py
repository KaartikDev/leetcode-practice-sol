class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #Create the return string
        myStr = ""
        i = 0

        #Make sure we dont go out of bounds for either word
        while i < len(word1) and i < len(word2):
            #add alternating letters
            myStr += word1[i] + word2[i]
            i+=1
        #include remaining string if different len
        myStr += word1[i:] + word2[i:]

        return myStr