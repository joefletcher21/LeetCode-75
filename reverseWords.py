class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        words = []
        result = ""
        for c in (s + " "):
            if c == " " and word is not "":
                words.append(word)
                word = ""
            elif c == " ":
                continue
            else:
                word += c
        i = len(words)-1
        while(i > 0):
            result += words[i] + " "
            i-=1
        result += words[0]
        return (result)
