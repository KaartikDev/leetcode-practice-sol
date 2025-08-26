# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Trying the fast/slow pointer traversal.
        if head is None or head.next is None: #Check for empty or single node lists
            return None
        
        #When fastP hits end the slowP at mid
        fastP = head #increment by 2
        slowP = head #incrmemebr by 1
        prev = None #behind slowP


        # print(slowP.val,fastP.val)
        while fastP and fastP.next:
            prev = slowP
            slowP = slowP.next
            fastP = fastP.next.next

        
        prev.next = slowP.next #skip a node to delete

        return head

        """
        Discussion:
        O(n) time complexity as fast/slow pointer tarverse list
        O(1) space complexity
        """