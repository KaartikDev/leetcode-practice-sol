class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        
        currIndex = 0
        currMax = 0

        windowSum = sum(nums[currIndex:currIndex+k])
        
        currMax = windowSum
        currIndex+=1
        # print(windowSum)

        while currIndex+k-1 < len(nums):
            windowSum -= nums[currIndex-1]
            windowSum += nums[currIndex+k-1]
            if windowSum > currMax:
                currMax = windowSum
            currIndex+=1
        
        """
        Discussion:
        O(n) time complexity
        O(1) space complexity 
        """
        return float(currMax)/k