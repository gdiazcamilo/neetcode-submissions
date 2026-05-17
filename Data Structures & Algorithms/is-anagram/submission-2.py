from collections import Counter, defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = defaultdict(int)
        for char in s:
            sCounter[char] += 1
        
        tCounter = defaultdict(int)
        for char in t:
            tCounter[char] += 1

        if len(sCounter) != len(tCounter):
            return False
            
        for k,v in sCounter.items():
            if tCounter[k] != v:
                return False
        
        return True