class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        allowedFlips = k
        
        maxWindow = 0
        startPointer = 0
        endPointer = 0

        while endPointer < len(nums):
            if nums[endPointer] == 1:
                endPointer+=1
            elif nums[endPointer] == 0 and allowedFlips > 0:
                allowedFlips-=1
                endPointer+=1
            else:
                if nums[startPointer] == 0: #free a zero flip and shrink window
                    startPointer+=1
                    allowedFlips+=1
                else: #shrink window
                    startPointer+=1
            
            if (endPointer-startPointer > maxWindow):
                maxWindow = endPointer-startPointer
        
        return maxWindow

        """
        Discussion:
        O(n) time complexity
        O(1) space complexity
        """
            
                
            

