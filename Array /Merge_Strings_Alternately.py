class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedStr = ""
        for i in range(len(word1)):
            mergedStr+= word1[i]
            if i in range(len(word2)):
                mergedStr+= word2[i]
        if len(word2) > len(word1):
            mergedStr+=word2[len(word1):]
        return mergedStr
