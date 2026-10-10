class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap = {}
        for ch in s: 
            hashmap[ch] = hashmap.get(ch, 0) + 1

        print(hashmap)

        for ch in t:
            if ch in hashmap:
                hashmap[ch] = hashmap.get(ch) - 1

                if hashmap.get(ch) == -1:
                    return False
            else:
                return False

        return True