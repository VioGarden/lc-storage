def convertToTitle(columnNumber):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    while columnNumber:
        columnNumber = columnNumber - 1
        ans = letters[columnNumber%26] + ans
        columnNumber = columnNumber//26
    return ans