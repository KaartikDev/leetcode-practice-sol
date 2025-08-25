import collections
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        r_index_q = collections.deque()
        d_index_q = collections.deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                r_index_q.append(i)
            else:
                d_index_q.append(i)
        
        while r_index_q and d_index_q: #Using thrutiness rules
            curr_r = r_index_q.popleft()
            curr_d = d_index_q.popleft()

            if curr_r < curr_d:
                r_index_q.append(curr_r+len(senate)) #ban d
                # space by + n to ensure same next round order
            else:
                d_index_q.append(curr_d+len(senate)) #ban r
                # space by + n to ensure same next round order
        
        if r_index_q:
            return 'Radiant'
        else:
            return "Dire"

        """
        Discussion: 
        O(n) time complexity, number of ban is limited to n-1
        O(n) space complexity
        """



        
        
        