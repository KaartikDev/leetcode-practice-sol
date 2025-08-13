class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # here is my idea 1:
        #List vw is a list of all the vowels
        #List pos is the position of all the vowels in orignal word
        #Reverse vw or remove chacrers in reverse order
        #THen rebuild a new string via adding letters form the orignal
        # unless the current add positon is in the possition array
        # all_vowel = ['a','e','i','o','u']

        #Idea 1 was too slow and hitting max time. I belive it is because python had to do a O(n)
        # for each time in was used

        #Here is idea 2
        #Still make a list of vowels in order
        #Then rebuild the string
        #if the current chacter is a vowel use the last elemtn in vowel list
        #Pop the last element in vowels
        #continue

        """
        Discussion:
        This solution takes O(n) time complexity because it checks each letter one at a time. 
        It takes O(n) space complexity because it creates a vowel list which, in the worst case, 
        can be the entire string. Since strings are immutable in Python, the new string is first 
        created as a list and then converted to a string only once.
        """
        vw = []
        newStr = list(s)
        for i in range(len(s)):
            l = s[i].lower()
            if(l == 'a' or l == 'e' or l == 'i' or l=='o' or l=='u'):
                vw.append(s[i])

        for i in range(len(s)):
            l = s[i].lower()
            if(l == 'a' or l == 'e' or l == 'i' or l=='o' or l=='u'):
                newStr[i] = vw.pop()
    
        return "".join(newStr)