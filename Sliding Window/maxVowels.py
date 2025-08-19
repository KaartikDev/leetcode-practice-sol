class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowelCount = 0
        vowels = 'aeiou'
        for i in range(k):
            if s[i] in vowels:
                vowelCount+=1
        
        maxCount = vowelCount
        currIndex = 1

        while currIndex+k-1<len(s):
        
            if s[currIndex-1] in vowels:
                vowelCount-=1
            if s[currIndex+k-1] in vowels:
                vowelCount+=1
            currIndex+=1

            if vowelCount > maxCount:
                maxCount = vowelCount
        
        return maxCount

        """
        Discussion:
        O(n) time complexity
        O(1) space complexity
        """