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
        leftProds = list(nums)
        rightProds = list(reversed(nums))
        # print(leftProds)
        # print(rightProds)

        curLeftProd = leftProds[0]
        curRightProd = rightProds[0]
        # print("START")
        for i in range(1,len(nums)):
            tempLeft = leftProds[i]
            leftProds[i] = curLeftProd
            curLeftProd = curLeftProd*tempLeft
            # print(leftProds)


            tempRight = rightProds[i]
            rightProds[i] = curRightProd
            curRightProd = curRightProd*tempRight
            
            # print(rightProds)
            # print("LOOP")

        rightProds = rightProds[::-1]

        ans = list(nums)

        for i in range(len(nums)):
            
            if i == 0:
                ans[i] = rightProds[i]
            elif i == len(nums)-1:
                ans[i] = leftProds[i]
            else:
                ans[i] = leftProds[i]*rightProds[i]


        return ans

        """
        Discussion:
        This solution runs in O(n) time because we scan the array twice: once to build products to the left of each index and once to multiply in products to the right. 
        The extra space is O(1) if we reuse the output array for left products and keep only a single running right product (the output array does not count toward space). 
        The method avoids division and handles zeros implicitly because the left/right products include any zeros outside the current index.
        """        