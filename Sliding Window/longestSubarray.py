class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        startPointer = 0
        endPointer = 0
        allowedSkips = 1
        maxWindow = 0

        while endPointer < len(nums):
            if nums[endPointer] == 1:
                endPointer+=1
            elif nums[endPointer] == 0 and allowedSkips > 0:
                allowedSkips-=1
                endPointer+=1
            else:
                if nums[startPointer] == 0: #shrink window size and free skip
                    allowedSkips+=1
                    startPointer+=1
                else: #shrink window size
                    startPointer+=1
            
            if (endPointer-startPointer > maxWindow):
                maxWindow = endPointer-startPointer
        
        if maxWindow == 0:
            return 0
        else:
            return  maxWindow-1 #need -1 to account for deleted element
        

        """
        Discussion:
        O(n) time complexity
        O(1) space complexity
        """