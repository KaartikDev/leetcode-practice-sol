# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """        

        if not root: #emptry tree return
            return None

        if p is root or q is root: #if either target is root then its the lca
            return root
        

        leftHas = self.lowestCommonAncestor(root.left, p,q) #see if left has p or q
        rightHas = self.lowestCommonAncestor(root.right,p,q) #see if right has p or q

        if leftHas and rightHas: #if left and right have a p or q then current node must be ans
            return root
        
        return leftHas or rightHas #only leftHas both p and q OR only rightHas both p and q
        """
        O(n) time complexity as we visit each node
        O(h) space complexity
        """

            
    