class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallStr = ""
        largeStr = ""
        if len(str1) < len(str2):
            smallStr = str1
            largeStr = str2
        else:
            smallStr = str2
            largeStr = str1
        while len(smallStr) is not 0:
            if largeStr.replace(smallStr,"") == "" and smallStr.replace(smallStr,"") == "":
                return smallStr
            smallStr = smallStr[:-1]
        return ""
