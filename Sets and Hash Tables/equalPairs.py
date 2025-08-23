class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Tuples ARE hashable because they are immutable
        row_frq = {}
        curr_col = []
        count = 0

        for i in range(len(grid)):
            row_tuple = tuple(grid[i])
            if row_tuple not in row_frq: #building row freq map
                row_frq[row_tuple] = 1
            else:
                row_frq[row_tuple] += 1
            
        
        for i in range(len(grid)): #building curr col
            for j in range(len(grid)): 
                curr_col.append(grid[j][i])
            
            col_tuple = tuple(curr_col) #convert to hashable type
            curr_col = []
            if col_tuple in row_frq: #add the number of identical rows
                count += row_frq[col_tuple]
        
        return count
        """
        Discussion:
        O(n^2) time complexity (n^2 to access every elemnt and O(1) look up time in has tables)
        O(n^2) dpace complexity (you make n-long row n times in freq map)
        """
        



            
        
        