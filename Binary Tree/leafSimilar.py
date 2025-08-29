# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        # Idea: Do a pre order traveal for one tree. Create a list appending only leaf nodes (no left no right) while traversal. Start travesing other tree pre order. if order/entry does not macth lists return false. if all macth return true

        firstTreeNode = root1
        secondTreeNode = root2
        myStack = []
        leaves1 = []
        leaves2 = [] 
        
        while firstTreeNode or myStack: #doing in order travesal
            while firstTreeNode:
                myStack.append(firstTreeNode)
                firstTreeNode = firstTreeNode.left #go down left side
            
            firstTreeNode = myStack.pop() #get back to last exist node
            if not firstTreeNode.left and not firstTreeNode.right: #process node(check if leaf)
                leaves1.append(firstTreeNode.val)
            firstTreeNode = firstTreeNode.right
        
        myStack = []

        while secondTreeNode or myStack:
            while secondTreeNode:
                myStack.append(secondTreeNode)
                secondTreeNode = secondTreeNode.left #go down left side
            
            secondTreeNode = myStack.pop() #get back to last exist node
            if not secondTreeNode.left and not secondTreeNode.right: #process node(check if leaf)
                leaves2.append(secondTreeNode.val)
            secondTreeNode = secondTreeNode.right
            
        
        # print(leaves1)
        # print(leaves2)

        return leaves1 == leaves2
        """
        Discussion:
        O(n1 + n2) time compelxity as we vist each node and check it
        O(h1+h2+l1+l2) we create stacks of heights (h1/h2) and number of leaves(l1/l2) in trees
        """
            
        