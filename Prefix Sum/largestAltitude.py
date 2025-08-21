class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxAlt = 0
        currAlt = 0

        for i in range(len(gain)):
            currAlt+=gain[i] #Keep a running sum
            if currAlt > maxAlt: #Save highest point
                maxAlt = currAlt
        
        return maxAlt

        """
        Discussion:
        O(n) time complexity
        O(1) space complexity
        """
        