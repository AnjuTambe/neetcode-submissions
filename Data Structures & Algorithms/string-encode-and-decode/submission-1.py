class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs: # ["neet", "code"]
            result += str(len(word)) + "#" + word  # result = [ "4#neet4#code" ]
        return result    


    def decode(self, s: str) -> List[str]:

        # ["4 # n e e t 4 # c o d e"]
        #   0         6

        result = []

        i = 0

        while i < len(s) : 

            j = i

            while s[j] != "#" : 
                j = j+1

            length =  int(s[i : j])    # get the integer start at i end at j [0 : 1]

            word_start = j+1   #2  start at 2 index 
            word_end  = j+1 + length  # 2 + 4 = 6  end at 6th index

            result.append(s[ word_start : word_end])

            i = word_end

        return result     

    