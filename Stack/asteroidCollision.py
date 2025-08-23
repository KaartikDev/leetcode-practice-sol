class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []
        i = 0
        curr_move_left = False
        prev_move_right = True
        while i < len(asteroids):
            if len(stack) == 0:
                stack.append(asteroids[i])
                i+=1
                continue 
                        
            currAsteroid = asteroids[i]
            if currAsteroid < 0:
                curr_move_left = True
            else:
                curr_move_left = False

            
            prevAsteroid = stack.pop()
            if prevAsteroid < 0:
                prev_move_right = False
            else:
                prev_move_right = True
            
            if (curr_move_left and prev_move_right): #opposite directions
                
                if (abs(prevAsteroid) > abs(currAsteroid)): #prev destroys current, add previous back and move on
                    stack.append(prevAsteroid)
                    i+=1
                elif (abs(prevAsteroid) == abs(currAsteroid)): #destroy each other so add nothing, move on
                    i+=1
                else: #previous destroyed, do not move onto next asteroid
                    pass

            else: 

                stack.append(prevAsteroid)
                stack.append(currAsteroid)
                i+=1
        
        return stack
        """
        O(n) time and space complexity
        """
            




        