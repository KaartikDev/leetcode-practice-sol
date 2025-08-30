# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.globalMax = 0 #initilize global max

        def curZigZag(node, dir, currPath):
            if not node:
                return 0 #empty tree

            currPath += 1 #Increase the length

            if currPath > self.globalMax: #update the global max
                self.globalMax = currPath

            if dir == 'right':
                curZigZag(node.left, 'left', currPath) #contunue previous path
                curZigZag(node.right, 'right', 0) #start a new path from this node
            else:
                curZigZag(node.left, 'left', 0) #start a new path from this node
                curZigZag(node.right, 'right', currPath) #contunue previous path
                #on first iter both calls have a currPath of 0

            

        curZigZag(root, '', -1) #start at -1 so after root node is zero(edges count for this problem)

        return self.globalMax
        """
        O(n) time complexity
        O(h) space complexiy
        """
