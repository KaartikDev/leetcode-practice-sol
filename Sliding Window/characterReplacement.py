class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1: #empty/single char only gaurd
            return len(s)
        
        # freqMap = {}
        # for c in s:
        #     freqMap[c] = 0
        

        maxLenFound = 1
        l = 0
        r = 0
        freqMap = {}
        while r < len(s):
            # print(s[l:r+1])

            if s[r] not in freqMap: #maintain a frequency count of the current substring
                    freqMap[s[r]] = 1
            else:
                    freqMap[s[r]] += 1
            
            tempFreqMax = 0
            for key in freqMap: #find the most frequent count(bounded by <= 26 unqiue english letters)
                if freqMap[key] > tempFreqMax:
                    mostCommonChar = key
                    tempFreqMax = freqMap[key]
            
            while (r-l+1) - tempFreqMax > k: #invalid window when the length of subtring - most frequent character is > k(max flips allowed)
                freqMap[s[l]] -= 1
                l+=1                    
            
            maxLenFound = max(r-l+1, maxLenFound)
            r+=1
        return maxLenFound
        """
        Time complexity: O(N)
        Space Complxity: O(M) M is num of unique letters
        """



        
