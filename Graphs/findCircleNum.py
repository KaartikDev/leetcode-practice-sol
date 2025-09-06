class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        visited = set() #set of visited nodes
        newFind = 0 #every time we encounter a new node NOT IN viisted already its a new province
        

        for i in range(len(isConnected)): #must check every city
            if i not in visited: #increasing province count and starting dfs search if we hit a newly found node
                newFind+=1
                visited.add(i) #add it to visited nodes
            
                nodeStack = [i] #do a dfs starting at the current node
                while nodeStack:
                    curr_I = nodeStack.pop() #the j from each iter turn into i as we continue searching
                    for j in range(len(isConnected)):
                        if isConnected[curr_I][j] == 1 and j not in visited: #only care about searching connected NEW nodes, already searched visited ones
                            nodeStack.append(j)
                            visited.add(j)
            
        return newFind
        """
        O(n^2) time complexity as this is a adjaceny matrix where we check i and j 
        O(n) space complexity
        """

        
