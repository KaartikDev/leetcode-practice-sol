class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        currGroupLen = 1
        currChar = chars[0] #Constraint says no empy list
        writeInd = 0
        i = 1
        while i < len(chars):
            if chars[i] == currChar: #Update length for consecutive charcater
                currGroupLen+=1
            else:
                chars[writeInd] = currChar #Inplace write character
                writeInd += 1 #Update write index
                if currGroupLen > 1: 
                    for d in str(currGroupLen): #Break int into each digit
                        chars[writeInd] = d
                        writeInd += 1

                    currGroupLen = 1 #Reset group length
                currChar = chars[i]
            i += 1
        
        # Adding last letter group
        chars[writeInd] = currChar
        writeInd+=1
        if currGroupLen > 1:
            for d in str(currGroupLen):
                chars[writeInd] = d
                writeInd += 1

        # This solves in O(n) time complexity 
        # Constant time complexity O(1) with len(chars) < 2k charcetrs as curr length is maxed at 4 long

        return writeInd

        