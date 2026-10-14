class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        seen = set()
        l = 0
        longest = 0

        for r in range(n) : 
           #while loop is only for removing duplicates until the window becomes valid again 
           while s[r] in seen : 
            seen.remove(s[l]) 
            l += 1

            # if window is valid 
           w = (r - l) + 1

           longest = max (longest , w)
           seen.add(s[r])
            
        return longest    


            



