class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #Live problem solving
        # One way to solve this problem is as follows:
        # Create a running total of possible flowers you can plant
        # Everytime you find a possible plantable location increase your pointer location by 2 
        # as you can not plant flowers next each other
        # Repeat this until your location is beyond string list OR runnign total >= n goal flowers

        #A possible plantable location has a 0 or list end on both sides
        # hard code a check for being on list ends
        #Many edge cases
        #Short lists empty lsit etc
        currNewFlowers = 0
        i = 0

        # while(i < len(flowerbed)):
        #     if (i == 0):
        #         if(flowerbed[i] == 0): 
        #             if (len(flowerbed)>i+1):
        #                 if(flowerbed[i+1] == 0):
        #                     currNewFlowers+=1
        #                     flowerbed[i] = 1
        #                     i+=2
        #                 else:
        #                     i+=2
        #             else:
        #                 currNewFlowers += 1
        #                 flowerbed[i] = 1
        #                 i+=2
        #         else:
        #             i+=2
        #     else:

        #         if(flowerbed[i] == 0):
        #             if (len(flowerbed)>i+1):
        #                 if(flowerbed[i+1] == 0 and flowerbed[i-1] == 0):
        #                     flowerbed[i] = 1
        #                     currNewFlowers+=1
        #                     i+=2
        #                 else:
        #                     i+=2
        #             else:
        #                 if(flowerbed[i-1] == 0):
        #                     flowerbed[i] = 1
        #                     currNewFlowers += 1
        #                 i+=2
        #         else:
        #             i+=2
        
        # if len(flowerbed) > 2:
        #     if(flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2]==0):
        #         flowerbed[len(flowerbed)-1] = 1
        #         currNewFlowers+=1


        ## NEW STRATEGY:
        # Check each spot one by one
        # If no adjacent flowers upadte it to 1, increase running total, increase index
        #Account for the edge case of begging and end of list

        #hardcode check for lists of length 1
        if(len(flowerbed)==1):
            if(flowerbed[0]==0):
                return 1>=n
            else:
                return 0>=n
        
        while(i<len(flowerbed) and currNewFlowers<n):
            if(i==0):
                if(flowerbed[i]==0 and flowerbed[i+1]==0):
                    flowerbed[i] = 1
                    currNewFlowers+=1
            elif (i==len(flowerbed)-1):
                if(flowerbed[i]==0 and flowerbed[i-1]==0):
                    flowerbed[i] = 1
                    currNewFlowers+=1
            else:
                if(flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
                    flowerbed[i] = 1
                    currNewFlowers+=1
            i+=1

        """
        Discussion:
        This solution is O(n) time and has constant space complexity. This is because we check    
        each element one at a time.
        """


        return (currNewFlowers>=n)


            

        