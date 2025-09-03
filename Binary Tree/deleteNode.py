# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def nextNum(root):
            if not root:
                return None
            
            curr = root.right
            while curr and curr.left:
                curr = curr.left
            return curr
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
            return root
        else:
            #Only gets here when key == root.val
            
            #Case 1 no children nodes
            if not root.left and not root.right:
                return None
            #Case 2.1 only left child
            if not root.right:
                return root.left
            #Case 2.2 only right child
            if not root.left:
                return root.right
            
            #Case 3 has 2 children
            succesorNode = nextNum(root)
            root.val = succesorNode.val
            root.right = self.deleteNode(root.right, succesorNode.val)
            return root
            """
            O(h) time complexity
            O(h) space compelxity because of recursive calls
            """
