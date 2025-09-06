class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        keysStack = []
        visited= {0}
        
        for i in range(len(rooms[0])):
            keysStack.append(rooms[0][i])
        

        while keysStack:
            # print(keysStack, visited)
            currKey = keysStack.pop()
            # print(currKey)
            if currKey not in visited:
                # print("NEW ROOM")
                visited.add(currKey)
                for i in range(len(rooms[currKey])):
                    keysStack.append(rooms[currKey][i])
        
        # print(visited)
        if len(visited) == len(rooms):
            return True
        else:
            return False
        """
        O(n+E) time complexity as we check each room, E = edges <= 3000 by constraints
        O(n) space complexity
        """