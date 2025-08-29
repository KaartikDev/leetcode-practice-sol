# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        def countFrom(root,targetSum): #calculates all the paths that START at ROOT node
            count = 0
            if not root:
                return 0
            if root.val == targetSum:
                count+=1 
        
            rootIncLeftAns = countFrom(root.left,targetSum-root.val) #include root via subtracting from target 
            rootIncRightAns = countFrom(root.right,targetSum-root.val) #include root via subtracting from target 
            return count + rootIncLeftAns + rootIncRightAns

        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0

        rootAns = countFrom(root, targetSum) #calculate all the paths including root
         
        leftAns  = self.pathSum(root.left, targetSum) #calculating paths that start at left subtree (no root inclusion as targetSum original)
        rightAns  = self.pathSum(root.right, targetSum) #calculating paths that start at right subtree (no root inclusion as targetSum original)
        
        return leftAns + rightAns + rootAns
        """
        O(n^2) time complexity
        O(h) space complexity 
        """

        
        
        