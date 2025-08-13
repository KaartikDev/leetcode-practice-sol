class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        """
        Discussion:
        Finding the original max candy count with max() is O(n), since it must
        scan the entire list once. The while loop also iterates through all n kids,
        making O(n) comparisons. Since these operations happen sequentially, the
        overall time complexity is O(n).
        """
        maxCandy = max(candies)
        results = []
        i = 0
        while (i<len(candies)):
            ans = (candies[i]+extraCandies>=maxCandy)
            results.append(ans)
            i+=1
        # print(results)
        return(results)
