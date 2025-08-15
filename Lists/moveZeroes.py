class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        check_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[check_index]
                nums[check_index] = temp
                check_index+=1
        """
        Time complexity of O(n), iterate through entire arr
        Space complexity O(1)
        """