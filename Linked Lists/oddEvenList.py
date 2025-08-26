# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next: #Empty or single node lists
            return head

        # tailP = head
        # n = 0
        # while tailP.next:
        #     tailP = tailP.next #stop at last node
        #     n+=1
        # n+=1 # get number of nodes
        # # print("num nodes is",n)
        
        # currP = head
        # prev = None
        # evenInd = 1
        # i = 0
        # while i < n and currP and currP.next:
        #     # print("curr node index and value",i,currP.val)
        #     if i == evenInd:
        #         prev.next = currP.next #skip a node
        #         currP.next = None # break the link between even and odd
        #         tailP.next = currP #add even node to the tail
        #         tailP = tailP.next #move tail forward
        #         currP = prev.next #move to next node
        #         evenInd += 2 #update index of where to do shenanigans
        #     else:
        #         prev = currP
        #         currP = currP.next
            
        #     # print(head)
        #     i+=1

        # return head

        #Trying canonical sol
        oddTailP = head
        evenTailP = head.next
        reconnectNode = evenTailP
        # print(reconnectNode)
        while evenTailP and evenTailP.next:
            oddTailP.next = evenTailP.next # changing head (skip a node as even is one ahead)
            oddTailP = oddTailP.next # Reassign odd pointer to next odd (head same)
            evenTailP.next = oddTailP.next # changing head (skip a node)
            evenTailP = evenTailP.next #Reassign even pointer to next even (head same)
        oddTailP.next = reconnectNode

        return head
        """
        Discussion:
        O(n) time compelexity
        O(1) space complexity
        """


        