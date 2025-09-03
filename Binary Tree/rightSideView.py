# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 
import collections
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #How to do level order
        if not root:
            return []
        
        #Implement level order search with a queue
        nodesQueue = collections.deque()
        result = [] #an array of array, each element array is a level on BT
        curLevel = 0

        nodesQueue.append(root) #put the root in

        while nodesQueue:
            result.append([]) #create new level array

            for i in range(len(nodesQueue)):
                curr = nodesQueue.popleft() #get the current node
                result[curLevel].append(curr.val)

                if curr.left:
                    nodesQueue.append(curr.left)

                if curr.right:
                    nodesQueue.append(curr.right)
            curLevel+=1
        
        finalAns = []
        for currLevel in result: #Get the right most element for each level
            finalAns.append(currLevel[-1])
        return finalAns
        """
        O(n) time complexity as we access each node
        O(n) space complexity as we store entire tree
        """