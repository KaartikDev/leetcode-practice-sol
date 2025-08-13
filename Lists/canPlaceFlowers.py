class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        """
        Revised discussion:
        This solution takes O(n) time as it checks each element one at a time in the worst case. T 
        The space complexity os O(1) as no new data structres are used.
        """
        # Revised solution:
        i = 0
        m = len(flowerbed)
        runningSum = 0
        while (i<m and runningSum<n):
            if flowerbed[i] == 0: #Empty pot
                left_ok = i==0 or flowerbed[i-1]==0 #OR short circuts to avoid out of bounds 
                right_ok = i==m-1 or flowerbed[i+1]==0
                if(left_ok and right_ok):
                    runningSum+=1
                    i+=2
                    continue
            i+=1
        return(runningSum>=n)

            

        
    


            

        