class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currCount = maxCount = 0
        i = 0
        firstVowelIndex = len(s)
        for char in "aeiou":
            if s.find(char) != -1:
                firstVowelIndex = min(firstVowelIndex,s.find(char))
        if firstVowelIndex == len(s):
            return 0
        while i <= len(s)-k:
            substring = s[i:i+k]
            currCount = sum(1 for char in substring if char in "aeiou")
            maxCount = max(currCount,maxCount)
            i+=1
        return maxCount
