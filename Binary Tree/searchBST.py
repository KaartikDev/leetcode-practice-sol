# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        
        
        curr = root

        while curr and curr.val != val:
            # print(curr.val,val)
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        
        return curr
        """
        O(h) time complexity -> O(logn) for balnced tree O(n) for skew
        O(1) space complexity
        """

        
        