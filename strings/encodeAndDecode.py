class Solution:

    def encode(self, strs: List[str]) -> str:
        finStr = ""

        for word in strs:
            finStr += str(len(word)) + '#' + word #encoded sitring is of format WORDLENGTH + # + WORD
        # print(finStr)
        return finStr


    def decode(self, s: str) -> List[str]:
        if len(s) == 0: #an empty string means and empty list
            return []
        
        pointer = 0
        ans = []
        while pointer < len(s):
            currWordLen = ""

            while s[pointer].isdigit(): #Scan to get full lenth of word until hit #
                currWordLen+=s[pointer]
                pointer+=1
            
            currWord = s[pointer+1:pointer+1+int(currWordLen)] #splice input to get the word
            # print([s,currWord,pointer+2,pointer+2+currWordLen])
            ans.append(currWord) #store it in output
            pointer+=1+int(currWordLen) #increment pointer
        
        return ans