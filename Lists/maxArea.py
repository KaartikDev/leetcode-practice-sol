class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height)-1
        maxArea = 0
        currArea = 0
        while i < j:
            
            currArea = (j-i) * min(height[i],height[j])
            if currArea > maxArea:
                maxArea = currArea
            
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return maxArea
    
    """
    Discussion:
    O(n) time complexity
    O(1) space complexity
    """

        

