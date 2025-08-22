class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # If both words have the same frequency for each letter they are close
        # This is because we could swap characters around until they match

        if len(word1) != len(word2): #If lengths dont match frequency cant
            return False

        freq_map1 = {}
        freq_map2 = {}

        for c in word1:
            if c not in freq_map1:
                freq_map1[c] = 1
            else:
                freq_map1[c] += 1
        
        for c in word2:
            if c not in freq_map2:
                freq_map2[c] = 1
            else:
                freq_map2[c] += 1
        
        #Now we have to iterate through every single character and makse sure they all exist
        for c in word1:
            if c not in freq_map2:
                return False

        ## We can transform charcters by swapping frequency counts AKA frequency counts need to match given reordering
        freq_counts1 = list(freq_map1.values())
        freq_counts2 = list(freq_map2.values())
        freq_counts1.sort()
        freq_counts2.sort()

        return freq_counts1 == freq_counts2

        """
        Discussion:
        O(n+m) as we create each frequecny map. Our values() list is at most 26 charcters
        O(1) space complexity as at most lenght 26 dictionary
        """