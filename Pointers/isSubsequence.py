class Solution:
    subsequences = ["ace", "one", "prime"]
    targetStr = "cdnckjdncwcwwckkcfvjkrvbvbnvliasbvnfdbgnjoihrtiyureoqfjnbjbnrlkwwpxmnmcncmbvnrmxvnvifkmznsmesfnjngreiunojlsdkmvnsedme"
    results = []

    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif s == t or s == "":
            return True
        else:
            count = 0
            for i in range(len(t)):
                if count <= len(s) - 1:
                    if s[count] == t[i]:
                        count += 1
            return count == len(s)

    for s in subsequences:
        results.append(isSubsequence(s, targetStr))

    print(results)
