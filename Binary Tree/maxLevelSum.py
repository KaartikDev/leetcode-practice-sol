# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 
import collections
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        result = []
        nodesQueue = collections.deque()
        currLevel = 0

        if not root:
            return 0
        
        nodesQueue.append(root)

        while nodesQueue:
            level_length = len(nodesQueue)
            result.append([]) #must start new empty level array
            
            for i in range(level_length):
                currNode = nodesQueue.popleft()
                result[currLevel].append(currNode.val)

                if currNode.left:
                    nodesQueue.append(currNode.left)

                if currNode.right:
                    nodesQueue.append(currNode.right)
                
            currLevel+=1
        maxSum = (root.val)
        highestSumLevel = 0
        for i in range(1,len(result)):
            currSum = sum(result[i])
            if currSum > maxSum:
                maxSum = currSum
                highestSumLevel = i

        return highestSumLevel + 1 #need +1 as our result array is zero-indexed but expected is 1 indexed 
        """
        O(n) time complexity
        O(n) space complexity
        """