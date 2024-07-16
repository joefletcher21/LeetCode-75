class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ""
        vowels = []
        for c in s:
            if c.lower() in "aeiou":
                vowels.append(c)
        vowels.reverse()
        print(vowels)
        index = 0
        for c in s:
            if c.lower() in "aeiou":
                result += vowels[index]
                index+=1
            else:
                result += c
        return result
