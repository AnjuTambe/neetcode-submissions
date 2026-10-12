from collections import defaultdict
class Solution:
  # # TC : O(n * k log k)
  #   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

  #     groups = defaultdict(list)

  #     for word in strs :
  #        sorted_word = "".join(sorted(word))

  #        groups[sorted_word].append(word)

  #     return list(groups.values())   
       
      def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs : 

          count = [0] * 26

          for ch in word : 

            index = ord(ch) - ord('a')
            count[index]+=1

          # after whole word finishing then count the tuple and store                     defaultdict
          key = tuple(count)
          groups[key].append(word)  

        return list(groups.values())     








             # group = {
                     
              #[1 , 0 , 1 , 1] : "cat , act"
              # []              : 

              #}







         


          

  
  
  
  
  
  
  
  
  
  
  
  
  # group = {
      
  
  #}    