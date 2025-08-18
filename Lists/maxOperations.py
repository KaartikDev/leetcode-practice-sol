class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #inital bodunry check

        if len(nums) < 2:
            return 0

        i = 0
        j = len(nums)-1
        total = 0
        currSum = 0
        nums.sort()
        while i<j:
            currSum = nums[i] + nums[j]
            # print(i,j,currSum)
            # print(nums[i],nums[j])
            if currSum == k:
                i+=1
                j-=1
                total+=1
                # print("FOUND")
            elif currSum < k: #Goal is larger than current (NEED TO MOVE SMALLER SIDE)
                if nums[i] < nums[j]: #element at i is the smaller side
                    i+=1
                else:
                    j-=1
            else: #Goal is smaller than current (NEED TO MOVE LARGER SIDE)
                
                if nums[i] < nums[j]: #element at j is the smaller side
                    j-=1
                else:
                    i+=1
        return total

        """
        Discussion
        Time complexity is O(nlogn) as we sort the array 
        Space complexity is O(1) as we sort in place. Nums is modified for this sol.
        """

 

        