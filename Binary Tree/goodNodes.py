# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        nodeStack = []
        branchMax = root.val #root existence garunteed
        curr = root
        count = 0
        while curr or nodeStack:
            while curr: #move down left brnach
                if curr.val >= branchMax: #maintain branch max
                    branchMax = curr.val
                nodeStack.append((curr,branchMax)) #save the node and its ancestor max in stack
                curr = curr.left
            
            currTuple = nodeStack.pop() #return to last existing tuple
            curr = currTuple[0]
            branchMax = currTuple[1] 
            if curr.val >= branchMax: #see if the value >= ancestor max
                count+=1
                # print(curr.val)
                # print(branchMax)
            curr = curr.right
        return count
        """
        O(n) time complexity
        O(h) space complexity, h = height, O(n) skew tree and O(log(n)) balanced tree
        """



            
        