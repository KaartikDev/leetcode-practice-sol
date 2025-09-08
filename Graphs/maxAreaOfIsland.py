class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        currSize = 0 
        maxSize = 0

        st = []

        for i in range(len(grid)): #visit all spots on island 
            for j in range(len(grid[0])): #check grid[0] to get n cols
                
                if grid[i][j] == 1 and (i,j) not in visited: #new island hs been discovered

                    visited.add((i,j)) #add curr node to visited
                    currSize=1 #set current island size to 1
                    st = [(i,j)] #we need to do a dfs at this position
                    while st:
                        currNode = st.pop()
                        curr_i = currNode[0]
                        curr_j = currNode[1]
                        if curr_i-1 >= 0 and grid[curr_i-1][curr_j] == 1 and (curr_i-1,curr_j) not in visited: #spot above
                            st.append((curr_i-1,curr_j))
                            visited.add((curr_i-1,curr_j)) #mark spot as visited
                            currSize+=1
                        if curr_i+1 < len(grid) and grid[curr_i+1][curr_j] == 1 and (curr_i+1,curr_j) not in visited: #spot below
                            st.append((curr_i+1,curr_j))
                            visited.add((curr_i+1,curr_j))
                            currSize+=1
                        if curr_j-1 >= 0 and grid[curr_i][curr_j-1] == 1 and (curr_i,curr_j-1) not in visited: #spot left
                            st.append((curr_i,curr_j-1))
                            visited.add((curr_i,curr_j-1))
                            currSize+=1
                        if curr_j+1 < len(grid[0]) and grid[curr_i][curr_j+1] == 1 and (curr_i,curr_j+1) not in visited: #spot right (check grid[0] to get num cols or n)
                            st.append((curr_i,curr_j+1))
                            visited.add((curr_i,curr_j+1))
                            currSize+=1
                        
                    maxSize = max(currSize, maxSize)
            
        return maxSize
        """
        O(m*n) time complexity
        O(m*n) space complexity
        """

                    