import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        charFreqToWordsHash = {}

        for currStr in strs:
            count = [0] * 26 #creating an empty frequency count

            for c in currStr: #count the number of characters in each word
            #ord(c) --> oridnal of c gives unicode
                count[ord(c)-ord('a')] += 1 #maps chacrters to 0-25 as chacrters are gaurnteed to be lowercase english chars
            
            hashableCount = tuple(count)
            if hashableCount not in charFreqToWordsHash:
                charFreqToWordsHash[hashableCount] = [currStr]
            else:
                charFreqToWordsHash[hashableCount].append(currStr)
        
        ans = []
        for key in charFreqToWordsHash:
            ans.append(charFreqToWordsHash[key])
        return ans 
        
        #O(N*L) --> N is num strs L is longest str
        #O(N) --> we make one hash map with all the strings in it and count list of size 26(constant)

