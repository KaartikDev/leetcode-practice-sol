class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mySum = sum(nums)
        # print(mySum)
        leftSum = 0
        for i in range(len(nums)):
            # print(i, mySum -  leftSum - nums[i], leftSum)
            if leftSum == mySum - leftSum - nums[i]:
                return i
            
            leftSum+=nums[i]
        return -1
        """
        Discussion:
        O(n) time complexity
        O(1) space complexity
        Assumes following:
        No integer overflows and all values are integers
        """