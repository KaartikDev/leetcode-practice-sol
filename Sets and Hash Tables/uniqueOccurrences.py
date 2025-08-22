class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        freq_map = {}

        for i in range(len(arr)):
            if arr[i] not in freq_map:
                freq_map[arr[i]] = 1
            else:
                freq_map[arr[i]] += 1
        

        return len(freq_map.values()) == len(set(freq_map.values()))
        """
        O(n) time complexity
        O(n) space complexity
        """
        