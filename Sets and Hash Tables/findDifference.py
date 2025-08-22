class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        #Using python set (hash table implemented) sol
        nums1_set = set((nums1))
        nums2_set = set((nums2))
        

        nums1_ans = nums1_set - nums2_set
        nums2_ans = nums2_set - nums1_set

        return [list(nums1_ans),list(nums2_ans)]
        """
        Disucssion
        O(m+n) time complexity as we convert lists to sets and back
        O(m+n) space complexity as we create sets
        """
