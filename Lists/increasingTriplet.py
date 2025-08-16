
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Checks to make sure there is at least three numbers
        if len(nums) < 3:
            return False

        small = float('inf')
        medium = float('inf')
        
        
        for i in range(len(nums)):
            if nums[i] <= small: 
                small = nums[i]
            elif nums[i] <= medium:
                medium = nums[i]
            else:
                return True

        return False

        """
        O(n) time compelixty
        O(1) Space Complexity
        """