class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        substring = s[:k]
        currCount = maxCount = sum(1 for char in substring if char in "aeiou")
        
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                currCount -= 1
            if s[i] in "aeiou":
                currCount += 1
            maxCount = max(currCount,maxCount)
        return maxCount
