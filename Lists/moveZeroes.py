class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #If a zero is found pop it and append at end, do not increase index as arr shifts left
        #At most you can only have as manyc checks and number of elements
        num_checks = len(nums)
        index = 0
        while num_checks > 0:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
            num_checks -= 1
        return nums

        """
        Time complexity of O(n), iterate through entire arr
        Space complexity O(1)
        """