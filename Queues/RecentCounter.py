#Need to use a queue a FIFO data structure
import collections

class RecentCounter(object):
    
    def __init__(self):
        self.requests = collections.deque() #notice syntax

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # print(self.requests)
        self.requests.append(t)

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft() #keep deleting the oldest entries until they all good

        return (len(self.requests))
        """
        Discussion:
        O(1) time amortized (few pings between t and 3000-t) worst case O(n)
        O(1) amoritized space complexity worst case O(n)
        """ 
        


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)