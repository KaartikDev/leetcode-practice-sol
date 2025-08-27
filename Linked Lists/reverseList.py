# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head or not head.next: #Empty or single node edge case
            return head
        
        currNode = head
        nextNode = None
        prev = None
        while currNode: #suspicos
            # print(head)
            # print(currNode)
            nextNode = currNode.next # reassign/rememeber next node
            currNode.next = prev #break link and point backwards
            prev = currNode #reassign previous pointer forward
            currNode = nextNode # reassign curr node to next node
            
        head = prev
        return head
        """
        Discussion:
        O(n) time complexity
        O(1) space complexity
        """
        
            
