# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        currNode = root

        if not root: #empty tree base case
            return 0
        
        
        maxRight = 0
        maxLeft = 0

        #dont need check leaf existence as base case handles empty input
        maxRight = self.maxDepth(currNode.right) #recursively go down right side
        maxLeft =  self.maxDepth(currNode.left) #recursively go down left side
        
        return max(maxRight,maxLeft) + 1 #need +1 to build the counter each call
        
        """
        Discussion:
        O(n) time complexity as we need to visit each node
        O(h) space complexity where h is the tree height --> O(n) on skewed trees and O(log(n)) on balanced trees
        """
        