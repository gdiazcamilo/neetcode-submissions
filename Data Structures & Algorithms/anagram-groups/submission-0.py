class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = self.getKey(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())
    

    def getKey(self, word: str):
        letterCount = [0]*26
        for letter in word:
            letterIdx = ord(letter)-ord('a')
            letterCount[letterIdx] += 1
        return tuple(letterCount)