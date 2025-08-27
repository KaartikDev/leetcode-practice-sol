# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # n is garunteed to be >= 2 and n%2==0
        n = 0
        maxSum  = -1 #vals are garunteed to be >= 1
        counterP = head
        while counterP:
            n+=1
            counterP = counterP.next
        
        
        midInd = n/2
        print(n,midInd)

        midP = head
        
        i = 0
        while i < midInd and midP:
            connectP = midP
            midP = midP.next
            i+=1

        #now we need to reverse it
        secondHalf = midP
        prevP = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prevP
            prevP = secondHalf
            secondHalf = temp
        # note: head is disconnected from reversed nodes
        
        #compare sums
        right = prevP
        left = head
        while right:
            currSum = left.val + right.val
            if currSum > maxSum:
                maxSum = currSum
            right = right.next
            left = left.next
    
        return maxSum
        """
        Dicussion:
        O(n) time complexity 
        O(1) space complexity (in place reversal)
        """