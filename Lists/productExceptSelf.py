class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #Using hint 1:
        """
        Think how you can efficiently utilize prefix and suffix products to calculate the product 
        of all elements except self for each index. Can you pre-compute the prefix and suffix 
        products in linear time to avoid redundant calculations?
        """

        
        #Step 1: Finding the right products and storing in place list
        output = list(reversed(nums))
        curRightProd = output[0]
        for i in range(1,len(nums)):
            tempRight = output[i]
            output[i] = curRightProd
            curRightProd = curRightProd*tempRight
        output.reverse() 
        # print(output)

        #Step 2: Get a running scalar of the left side and multiply
        curLeftProd = 1
        for i in range(len(nums)):
            
            # print(curLeftProd,i)
            if i == 0:
                pass
            elif i == len(nums)-1:
                output[i] = curLeftProd
                # print("END", output[i])
            else:
                # print("MID1", output[i], curLeftProd)
                output[i] = output[i]*curLeftProd
                # print("MID2", output[i])
            curLeftProd = curLeftProd * nums[i]

        return output

        """
        Time complexity is O(n)
        Space complexity is O(1) not counting output array
        """

        