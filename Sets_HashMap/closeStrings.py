class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        letters1 = set(char for char in word1)
        letters2 = set(char for char in word2)
        maxCount1 = []
        maxCount2 = []

        for i in letters1:
            if i not in letters2:
                return False
            maxCount1.append(word1.count(i))
        for i in letters2:
            maxCount2.append(word2.count(i))
        maxCount1.sort()
        maxCount2.sort()
        if maxCount1 != maxCount2:
            return False
        print(maxCount1, maxCount2)
        return True
